from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, PlainTextResponse, FileResponse
import json
import os
import csv

app = FastAPI()

# Enable CORS for all origins (matching previous behavior)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

JSON_FILE = 'participants_master.json'
CSV_FILE = 'Hackathon participants final list.csv'

def save_csv(teams):
    """Maps the dashboard JSON data back to the original CSV format."""
    headers = [
        "Team ID", "Team Name", "Candidate's Name", "Candidate's Email", 
        "Candidate's Mobile", "Candidate's Location", "User Type", "Domain", 
        "Course", "Course Specialization", "Course Type", "Course Duration (years)", 
        "Year of Graduation", "Candidate's Organisation", "Differently Abled", 
        "Status", "Candidate's Report", "Report Link", "Round 1 Score"
    ]
    
    rows = []
    for t in teams:
        # Separate members: Leader first, then others
        sorted_members = sorted(t.get('members', []), key=lambda x: not x.get('isLeader', False))
        for m in sorted_members:
            rows.append({
                "Team ID": t.get('id', ''),
                "Team Name": t.get('name', ''),
                "Candidate's Name": m.get('name', ''),
                "Candidate's Email": m.get('email', ''),
                "Candidate's Mobile": m.get('phone', ''),
                "Candidate's Location": m.get('address', ''),
                "User Type": "Team Leader" if m.get('isLeader') else "Team Member",
                "Domain": "General",
                "Course": m.get('college', ''),
                "Course Specialization": m.get('dept', ''),
                "Course Type": "Technical",
                "Course Duration (years)": 4,
                "Year of Graduation": m.get('gradYear', ''),
                "Candidate's Organisation": m.get('college', ''),
                "Differently Abled": "No",
                "Status": t.get('status', 'In-progress'),
                "Candidate's Report": "Pending",
                "Report Link": "-",
                "Round 1 Score": t.get('score', 0)
            })
            
    try:
        with open(CSV_FILE, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()
            writer.writerows(rows)
        print(f"[*] Successfully synchronized {CSV_FILE}")
    except Exception as e:
        print(f"[!] CSV Sync Error: {e}")

@app.get("/", response_class=PlainTextResponse)
def health_check():
    """Health check endpoint for Render monitoring."""
    return "AX26 Sync Server is Online."

@app.get("/get-json")
def get_json():
    """Serves the latest participants_master.json."""
    if os.path.exists(JSON_FILE):
        return FileResponse(JSON_FILE, media_type="application/json")
    return JSONResponse(status_code=404, content={"message": "JSON file not found"})

@app.get("/get-csv")
def get_csv():
    """Serves the latest Hackathon participants final list.csv."""
    if os.path.exists(CSV_FILE):
        return FileResponse(CSV_FILE, media_type="text/csv", filename="ax26_master_export.csv")
    return JSONResponse(status_code=404, content={"message": "CSV file not found"})

@app.post("/save-json")
async def save_json(request: Request):
    """Saves the dashboard state to participants_master.json and CSV."""
    try:
        data = await request.json()
        # Ensure the file exists or create it
        with open(JSON_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
        
        # Synchronize CSV
        save_csv(data)
        
        print(f"[*] Updated {JSON_FILE} & {CSV_FILE} with current dashboard state.")
        return {"status": "success", "message": "Global Data Synchronized"}
    except Exception as e:
        print(f"[!] Error saving data: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    # Render and other platforms provide PORT environment variable
    PORT = int(os.environ.get('PORT', 8000))
    uvicorn.run(app, host="0.0.0.0", port=PORT)

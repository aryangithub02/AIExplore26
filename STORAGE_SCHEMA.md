# 💾 Data Storage Schema (localStorage)

The platform uses a client-side persistence layer based on `window.localStorage`. All data keys are prefixed with `hf_` to avoid collisions.

## 🛠️ DB Helper
A custom `DB` object handles JSON serialization and retrieval:
```javascript
const DB = {
  get: (k) => JSON.parse(localStorage.getItem("hf_" + k)),
  set: (k, v) => localStorage.setItem("hf_" + k, JSON.stringify(v)),
  del: (k) => localStorage.removeItem("hf_" + k)
};
```

---

## 📋 Data Collections

### 1. `users`
An array of user objects.
```typescript
interface User {
  id: string;          // u_ + timestamp
  name: string;
  email: string;       // Unique identifier for login
  password: string;
  college: string;
  department: string;
  phone: string;
  isAdmin: boolean;    // Role flag
}
```

### 2. `teams`
An array of team objects.
```typescript
interface Team {
  id: string;          // t_ + timestamp
  name: string;        // Unique
  code: string;        // 6-character unique code (HF-XXXXXX)
  leader: string;      // User ID of the creator
  members: string[];   // Array of User IDs
  createdAt: string;   // ISO date
}
```

### 3. `registrations`
An array of registration entries submitted by teams.
```typescript
interface Registration {
  id: string;          // REG- + unique string
  teamId: string;
  teamName: string;
  problem: string;     // ps1 | ps2 | ps3 | ps4
  problemTitle: string;
  projectName: string;
  description: string;
  techStack: string;
  status: 'Pending' | 'Approved' | 'Rejected';
  paid: boolean;
  submittedAt: string; // ISO date
}
```

### 4. `session`
The currently logged-in user object.
- Key: `hf_session`
- Value: `User` object or `null`.

### 5. `announcements`
The system announcements feed.
```typescript
interface Announcement {
  id: string;
  title: string;
  date: string;
  body: string;
}
```

---

## 🔑 Default Credentials

### Admin Account
- **Email:** `admin@AIExplore 2K26.com`
- **Password:** `admin123`

---

## ⚠️ Data Persistence Note
Since data is stored in `localStorage`, it is specific to the browser and device used. Clearing browser data will reset all registrations and user accounts.

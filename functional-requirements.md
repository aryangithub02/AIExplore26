# Hackathon Registration Website
## Functional Requirements Document

---

# 1. User Roles

1. Participant
2. Admin

---

# 2. Authentication

FR-1: Users must be able to register using:
- Full name
- Email
- Password
- College
- Department
- Contact number

FR-2: Users must be able to login using email and password.

FR-3: Admin login must be supported.

FR-4: Session must persist using localStorage.

---

# 3. Team Management

FR-5: A user must be able to create a team.

FR-6: Team name must be unique.

FR-7: A team must generate a unique team code.

FR-8: A user must be able to join a team using team code.

FR-9: Team size must not exceed defined limit.

FR-10: Team members list must update dynamically.

---

# 4. Registration

FR-11: Team must complete multi-step registration.

FR-12: Problem statement selection must be mandatory.

FR-13: Declaration checkbox must be mandatory.

FR-14: System must generate unique Registration ID.

FR-15: Registration status must default to "Pending".

---

# 5. Dashboard

FR-16: Dashboard must display:
- Registration status
- Team name
- Members count
- Payment status

FR-17: Announcements must be viewable.

---

# 6. Payment

FR-18: User must be able to simulate payment.

FR-19: Payment status must update after confirmation.

FR-20: Registration status may auto-update after payment.

---

# 7. Deadline Automation

FR-21: System must prevent registration after deadline.

FR-22: Countdown timer must update dynamically.

FR-23: Closed banner must appear after deadline.

---

# 8. Admin Panel

FR-24: Admin must view all teams.

FR-25: Admin must view all participants.

FR-26: Admin must approve/reject teams.

FR-27: Admin must export CSV.

FR-28: Admin must filter teams.

FR-29: Admin must search teams.

---

# 9. Notifications

FR-30: Success and error toasts must display.

FR-31: On successful registration, confirmation screen must appear.

---

# 10. Error Handling

FR-32: Invalid login must show error.

FR-33: Duplicate team name must show error.

FR-34: Invalid team code must show error.

---

END OF FUNCTIONAL REQUIREMENTS
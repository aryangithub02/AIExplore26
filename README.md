# 🚀 AIExplore 2K26 — Hackathon Registration Platform

AIExplore 2K26 is a premium, high-performance hackathon registration website designed with a modern tech aesthetic and a focus on visual excellence. This platform provides a seamless experience for participants to register, form teams, and manage their hackathon journey.

![Tech Stack](https://img.shields.io/badge/Stack-HTML5%20%7C%20CSS3%20%7C%20JS-blue)
![Theme](https://img.shields.io/badge/Theme-Dark%20Glow-purple)
![License](https://img.shields.io/badge/License-MIT-green)

---

## ✨ Key Features

### 🌟 Landing Experience
- **Dynamic Hero Section**: Features a high-impact headline and a live countdown timer to the registration deadline.
- **Glassmorphic UI**: Modern card designs for prizes, tracks, and timeline.
- **Interactive FAQ**: Smooth accordion animations for better UX.

### 🔐 Advanced Authentication
- **Secure Register/Login**: Real-time validation and session persistence using `localStorage`.
- **Role-Based Access**: Separate interfaces for Participants and Administrators.

### 👥 Team Management System
- **Create/Join Logic**: Generate unique team codes and invite friends.
- **Live Membership Tracking**: Real-time updates of team members in the dashboard.

### 📝 Multi-Step Registration
- **Intuitive Flow**: A seamless 3-step registration process capturing participant details, team info, and declarations.
- **Dynamic ID Generation**: Automatically generates a unique Registration ID for every team.

### 📊 Comprehensive Dashboard
- **Status Badges**: Visual indicators for registration and payment status.
- **Announcements**: Centralized feed for event updates.
- **Payment Simulation**: Interactive payment simulation to finalize entry.

### 🛠️ Powerful Admin Panel
- **Data Table Management**: View, filter, and search through all registered teams and participants.
- **Approval Workflow**: Approve or reject teams with a single click.
- **CSV Export**: Extract registration data for offline processing.

---

## 🛠️ Architecture & Tech Stack

The project follows a **Single-File Architecture** approach for maximum portability and speed.

- **Frontend**: 
  - Standard **HTML5 Semantic Elements** for SEO and accessibility.
  - **Vanilla CSS3** with custom properties (CSS Variables) for theme management.
  - **Modern Typography**: Inter and Syne fonts for a sharp, tech look.
- **Logic**: 
  - **Vanilla JavaScript (ES6+)**: Custom state management system handles authentication, form validation, and data persistence.
- **Database**: 
  - **localStorage Solution**: A custom DB wrapper simulates a real database, persisting user data across sessions without a backend.

---

## 🎨 Design System

| Entity | Value |
| :--- | :--- |
| **Primary Background** | `#0a0e1a` (Deep Slate) |
| **Primary Accent** | `#3b82f6` (Vibrant Blue) |
| **Secondary Accent** | `#8b5cf6` (Electric Purple) |
| **Typography** | Syne (Heads) / Inter (Body) |
| **Corner Radius** | `12px` (Soft Cards) / `8px` (Buttons) |

---

## 📂 Project Structure

```bash
AIExplore26/
├── index.html                # Main application (HTML/CSS/JS)
├── design-requirements.md    # UI/UX Specifications
├── functional-requirements.md # Business Logic & Rules
└── task.md                   # Project Roadmap & Status
```

---

## 🚀 Getting Started

Since this is a client-side application, getting started is simple:

1. **Clone the repository**:
   ```bash
   git clone [repository-url]
   ```
2. **Open the App**:
   Simply open `index.html` in any modern web browser.
3. **Admin Access**:
   - Navigate to the Login modal.
   - Use the designated Admin credentials (pre-configured in local storage or logic).

---

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

<p align="center">
  Built with ❤️ for the AI Community
</p>

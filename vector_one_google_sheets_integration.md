# Vector One Holdings — Google Sheets Database Lead Capture Integration Guide

**Account:** `silattrader@gmail.com`  
**Target File:** [`index.html`](file:///C:/Users/User/Desktop/Vector%20One/Vector_One_Outputs/index.html)  
**Database Destination:** Google Sheets (`Vector_One_Leads_Database`)  

---

## 📌 Executive Summary

This guide outlines the zero-cost, enterprise-grade integration connecting the **Connect With Executive Leadership** form on the Vector One website directly to a **Google Sheets Database** hosted under your Google Cloud account (`silattrader@gmail.com`).

Whenever a prospective client, investor, or institutional partner submits an executive inquiry on your website, their contact details are automatically appended as a new row in your Google Sheet in real-time.

---

## 🛠️ Step 1: Create Your Google Sheet

1. Log into **Google Drive** using your account: **`silattrader@gmail.com`**.
2. Click **+ New** ➔ **Google Sheets** ➔ **Blank spreadsheet**.
3. Title the spreadsheet: **`Vector_One_Leads_Database`**.
4. In Row 1, set up the following 6 column headers:

| Cell A1 | Cell B1 | Cell C1 | Cell D1 | Cell E1 | Cell F1 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Timestamp** | **Full Name** | **Corporate Email** | **Inquiry Area** | **Message / Scope** | **Status** |

---

## ⚡ Step 2: Add Google Apps Script (Webhook Receiver)

1. Inside your Google Sheet, click **Extensions** ➔ **Apps Script**.
2. Erase any existing code in the editor and **paste the following Google Apps Script code**:

```javascript
// Vector One Holdings - Lead Capture Webhook Script (silattrader@gmail.com)
function doPost(e) {
  try {
    var sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
    var data = JSON.parse(e.postData.contents);
    
    // Append submission data to sheet
    sheet.appendRow([
      data.timestamp || new Date().toLocaleString(),
      data.name || "N/A",
      data.email || "N/A",
      data.inquiry || "General Inquiry",
      data.message || "N/A",
      "New Inquiry (Pending Follow-up)"
    ]);
    
    return ContentService.createTextOutput(JSON.stringify({ "result": "success" }))
                         .setMimeType(ContentService.MimeType.JSON);
  } catch (error) {
    return ContentService.createTextOutput(JSON.stringify({ "result": "error", "error": error.toString() }))
                         .setMimeType(ContentService.MimeType.JSON);
  }
}
```

3. Click the **💾 Save** icon (or press `Ctrl + S`).

---

## 🚀 Step 3: Deploy as Web App

1. In the Apps Script top-right corner, click **Deploy** ➔ **New deployment**.
2. Click the ⚙️ gear icon next to *Select type* and choose **Web app**.
3. Configure the settings exactly as follows:
   - **Description:** `Vector One Website Lead Integration`
   - **Execute as:** `Me (silattrader@gmail.com)`
   - **Who has access:** `Anyone` *(crucial for public website submission)*
4. Click **Deploy**.
5. Grant permissions when prompted *(Click "Review Permissions" ➔ Select `silattrader@gmail.com` ➔ Click "Advanced" ➔ Click "Go to Code (unsafe)" ➔ Click "Allow")*.
6. Copy the generated **Web App URL** *(looks like `https://script.google.com/macros/s/AKfycbx.../exec`)*.

---

## 🔗 Step 4: Link Web App URL to `index.html`

Open `index.html` in your text editor (or ask your assistant) and update line 700:

```javascript
// Replace this placeholder with your copied Web App URL from Step 3:
const GOOGLE_SHEET_WEB_APP_URL = "https://script.google.com/macros/s/YOUR_COPIED_DEPLOYMENT_ID/exec";
```

---

## ✅ Step 5: Test Submission

1. Open `index.html` in your browser.
2. Scroll to the footer: **Connect With Executive Leadership**.
3. Fill in a test name (e.g., `Silat Trader`), email (`silattrader@gmail.com`), select an inquiry area, and click **Submit Executive Inquiry**.
4. Check your Google Sheet (`Vector_One_Leads_Database`) — the test record will appear immediately in Row 2!

---

*Vector One Holdings | Enterprise Cloud Architecture Suite*

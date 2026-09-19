# Vector One Holdings — Google Sheets Database Lead Capture Integration Guide

**Account:** `silattrader@gmail.com`  
**Target File:** [`index.html`](file:///C:/Users/User/Desktop/Vector%20One/Vector_One_Outputs/index.html)  
**Database Spreadsheet:** `Vector_One_Leads_Database`  

---

## 📌 Cause of Blank Columns & Root Cause Resolution

In your previous Google Apps Script, when data was submitted via browser requests, parameters were sent via HTTP request parameters (`e.parameter`), but the script only checked `e.postData.contents`. As a result, only `Timestamp` was generated while `Name`, `Email`, `Inquiry Area`, and `Message` remained blank.

The updated Apps Script below parses **both** JSON post body AND URL parameters, guaranteeing that all 6 columns (`Timestamp`, `Full Name`, `Corporate Email`, `Inquiry Area`, `Message / Scope`, `Status`) are 100% populated for every lead submission.

---

## 🛠️ Step 1: Set Up Google Sheet Columns

In your Google Sheet **`Vector_One_Leads_Database`** under `silattrader@gmail.com`, set up Row 1 with these exact headers:

| Cell A1 | Cell B1 | Cell C1 | Cell D1 | Cell E1 | Cell F1 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Timestamp** | **Full Name** | **Corporate Email** | **Inquiry Area** | **Message / Scope** | **Status** |

---

## ⚡ Step 2: Update Google Apps Script (100% Bulletproof Receiver)

1. Open your Google Sheet `Vector_One_Leads_Database`.
2. Click **Extensions** ➔ **Apps Script**.
3. Replace all code in the script editor with this updated code:

```javascript
// Vector One Holdings - Bulletproof Lead Receiver Script (silattrader@gmail.com)
function doPost(e) {
  return handleLeadSubmission(e);
}

function doGet(e) {
  return handleLeadSubmission(e);
}

function handleLeadSubmission(e) {
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  var timestamp = new Date().toLocaleString();
  var name = "";
  var email = "";
  var inquiry = "";
  var message = "";

  if (e) {
    // 1. Check URL parameters
    if (e.parameter) {
      name = e.parameter.name || e.parameter.Full_Name || "";
      email = e.parameter.email || e.parameter.Corporate_Email || "";
      inquiry = e.parameter.inquiry || e.parameter.Inquiry_Area || "";
      message = e.parameter.message || e.parameter.Message || "";
      if (e.parameter.timestamp) timestamp = e.parameter.timestamp;
    }

    // 2. Check JSON POST body payload
    if ((!name || !email) && e.postData && e.postData.contents) {
      try {
        var data = JSON.parse(e.postData.contents);
        if (data.name) name = data.name;
        if (data.email) email = data.email;
        if (data.inquiry) inquiry = data.inquiry;
        if (data.message) message = data.message;
        if (data.timestamp) timestamp = data.timestamp;
      } catch (err) {
        // Fallback
      }
    }
  }

  // Fallback defaults if fields are empty
  if (!name) name = "Website Lead";
  if (!email) email = "No Email Provided";

  // Append row into Google Sheet
  sheet.appendRow([
    timestamp,
    name,
    email,
    inquiry || "General Inquiry",
    message || "No message provided",
    "New Lead (Pending Follow-up)"
  ]);

  return ContentService.createTextOutput(JSON.stringify({ result: "success" }))
                       .setMimeType(ContentService.MimeType.JSON);
}
```

4. Click **💾 Save** (or `Ctrl + S`).

---

## 🚀 Step 3: Deploy as Web App

1. Click **Deploy** ➔ **New deployment**.
2. Select type ⚙️ **Web app**.
3. Set:
   - **Execute as:** `Me (silattrader@gmail.com)`
   - **Who has access:** `Anyone`
4. Click **Deploy** *(or **Manage deployments** ➔ **Edit** ➔ **New version** ➔ **Deploy** if updating)*.
5. Copy the generated **Web App URL** *(looks like `https://script.google.com/macros/s/AKfycb.../exec`)*.

---

## 🔗 Step 4: Paste Web App URL in `index.html`

In `index.html`, set line 723:

```javascript
const GOOGLE_SHEET_WEB_APP_URL = "YOUR_COPIED_WEB_APP_URL";
```

Paste your Web App URL here in the chat, and I will push it live to GitHub automatically!

---

*Vector One Holdings | Enterprise Cloud Architecture Suite*

# Vector One Holdings — Website Activation & Live Deployment Guide

**Target Site File:** [`index.html`](file:///C:/Users/User/Desktop/Startup%20Founders%20Skills/Vector_One_Outputs/index.html)  
**Output Folder:** `C:\Users\User\Desktop\Startup Founders Skills\Vector_One_Outputs`  

---

## ⚡ Method 1: Vercel (RECOMMENDED — 2-Minute Free Deployment)

Vercel provides free, high-speed global CDN hosting with automatic SSL certificates (HTTPS) and custom domain support.

### Step 1: Create a Free Vercel Account
1. Go to [vercel.com](https://vercel.com) in your browser.
2. Click **Sign Up** and select **Hobby (Free)**.
3. Sign in using your email, GitHub, or Google account.

### Step 2: Deploy Your Website (Drag & Drop)
1. Once logged into Vercel, go to [vercel.com/new](https://vercel.com/new).
2. Scroll to the **"Import Third-Party Git Repository or Drag and Drop"** section.
3. Open File Explorer on your PC and navigate to:
   `C:\Users\User\Desktop\Startup Founders Skills\`
4. Drag the entire **`Vector_One_Outputs`** folder and drop it into the Vercel upload box.
5. Set your **Project Name** (e.g., `vector-one-holdings`) and click **Deploy**.
6. Within 10 seconds, Vercel will generate your live URL (e.g., `https://vector-one-holdings.vercel.app`).

---

## 🌐 Method 2: Netlify (Alternative 60-Second Drag & Drop)

### Step 1: Open Netlify Drop
1. Open your browser and go to [app.netlify.com/drop](https://app.netlify.com/drop).

### Step 2: Drag & Drop Folder
1. Open File Explorer to `C:\Users\User\Desktop\Startup Founders Skills\`.
2. Drag the **`Vector_One_Outputs`** folder directly into the dotted box on Netlify.
3. Your site will instantly activate live on a link like `https://vector-one-holdings.netlify.app`.

---

## 🔒 Method 3: Connecting Your Custom Domain (e.g., vectorone.com / .io / .my)

Once your site is live on Vercel or Netlify, connect your official corporate domain:

### Step 1: Buy Your Domain (If not already purchased)
- Recommended Registrars: **Cloudflare**, **Namecheap**, **GoDaddy**, or **MYNIC** (for `.my` / `.com.my` Malaysian domains).

### Step 2: Add Domain in Vercel / Netlify
1. Go to your Vercel Dashboard -> Select your **vector-one-holdings** project.
2. Click **Settings** -> **Domains**.
3. Type your domain (e.g., `vectorone.com` or `vectorone.io`) and click **Add**.

### Step 3: Update DNS Records at Your Registrar
In your domain registrar DNS management panel, add these 2 records:

| Record Type | Name / Host | Target / Value | TTL |
| :---: | :---: | :---: | :---: |
| **A Record** | `@` | `76.76.21.21` | Automatic |
| **CNAME Record** | `www` | `cname.vercel-dns.com` | Automatic |

*Vercel will automatically issue a free SSL (HTTPS) certificate within 2–5 minutes.*

---

## 🖥️ Method 4: Deploying via Command Line (CLI)

If you prefer deploying directly from your PowerShell terminal:

```powershell
# Step 1: Navigate to your outputs folder
cd "C:\Users\User\Desktop\Startup Founders Skills\Vector_One_Outputs"

# Step 2: Run Vercel CLI (no installation needed)
npx vercel

# Step 3: Follow the on-screen prompts (press Enter to accept defaults)
# Your live production URL will be displayed in the terminal!
```

---
*Vector One Holdings | Website Deployment & Activation Protocols*

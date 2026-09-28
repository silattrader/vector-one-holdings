import base64
import os
import re

base_dir = r"c:\Users\User\Desktop\Vector One\Vector_One_Outputs"
html_path = os.path.join(base_dir, "index.html")

with open(html_path, "r", encoding="utf-8") as f:
    html_content = f.read()

images = {
    "vector_one_holdings_logo.jpg": "",
    "vector_aero_logo.jpg": "",
    "vector_compute_logo.jpg": "",
    "vector_intelligence_logo.jpg": "",
    "vector_academy_logo.jpg": "",
    "vector_brand_ecosystem.jpg": ""
}

for img_name in images:
    img_path = os.path.join(base_dir, img_name)
    with open(img_path, "rb") as f:
        b64 = base64.b64encode(f.read()).decode('utf-8')
        images[img_name] = f"data:image/jpeg;base64,{b64}"

print("All 6 images converted to base64 data URLs.")

# Rebuild the Brand Ecosystem section HTML cleanly with the exact brand logos matching the user's diagram
new_brand_ecosystem_html = f'''  <!-- VECTOR BRAND ECOSYSTEM & UNIT LOGOS -->
  <section id="brand-ecosystem" class="py-20 relative bg-slate-950/90 border-t border-b border-slate-800/80">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="text-center max-w-3xl mx-auto mb-16">
        <div class="inline-block px-3 py-1 rounded-md bg-cyan-500/10 text-cyan-400 text-xs font-mono mb-3 uppercase tracking-widest">CORPORATE ARCHITECTURE</div>
        <h2 class="text-3xl sm:text-4xl font-extrabold text-slate-100">Vector Brand Ecosystem</h2>
        <p class="text-slate-400 text-sm mt-3">Integrated specialization across defense, compute logistics, agentic intelligence, and talent development under Vector One Holdings.</p>
      </div>

      <!-- PARENT HOLDING LOGO BANNER -->
      <div class="mb-12 flex justify-center">
        <div class="glass-panel-glow p-6 sm:p-8 rounded-3xl max-w-3xl w-full text-center border border-cyan-500/40 bg-slate-900/90 shadow-2xl">
          <div class="text-xs font-mono text-cyan-400 uppercase tracking-widest mb-4 flex items-center justify-center space-x-2">
            <span class="w-2 h-2 rounded-full bg-cyan-400 animate-ping"></span>
            <span>PARENT / HOLDING COMPANY</span>
          </div>

          <div class="p-4 rounded-2xl bg-white flex items-center justify-center border border-slate-200 shadow-xl max-w-xl mx-auto">
            <img src="{images['vector_one_holdings_logo.jpg']}" alt="Vector One Holdings Brand Logo" class="h-24 sm:h-28 max-w-full object-contain">
          </div>
          <div class="text-xs font-mono text-cyan-300 mt-4 tracking-wider">CORPORATE REGISTRATION: SSM MALAYSIA INCORPORATED</div>
        </div>
      </div>

      <!-- 4 SUBSIDIARY BRAND LOGO CARDS MATCHING CORPORATE DIAGRAM -->
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 mb-16">
        
        <!-- CARD 1: VECTOR AERO -->
        <div class="glass-panel p-6 rounded-2xl text-center hover:border-amber-500/50 transition-all duration-300 group flex flex-col justify-between bg-slate-900/80">
          <div class="space-y-4">
            <div class="text-[11px] font-mono text-amber-400 uppercase tracking-wider font-semibold">Drone & Counter-UAS</div>
            <div class="bg-white p-4 rounded-2xl border border-slate-200 flex items-center justify-center min-h-[170px] shadow-lg group-hover:scale-[1.02] transition-transform duration-300">
              <img src="{images['vector_aero_logo.jpg']}" alt="Vector Aero Brand Logo" class="max-h-36 max-w-full object-contain">
            </div>
            <h3 class="text-lg font-bold text-slate-100">Vector Aero</h3>
            <p class="text-xs text-slate-400 leading-relaxed">Uncrewed Aerial Systems & Kinetic Perimeter Defense Solutions.</p>
          </div>
          <div class="mt-4 pt-3 border-t border-slate-800/80 text-[10px] font-mono text-slate-400 uppercase tracking-wider font-semibold">A MEMBER OF VECTOR ONE HOLDINGS</div>
        </div>

        <!-- CARD 2: VECTOR COMPUTE -->
        <div class="glass-panel p-6 rounded-2xl text-center hover:border-cyan-500/50 transition-all duration-300 group flex flex-col justify-between bg-slate-900/80">
          <div class="space-y-4">
            <div class="text-[11px] font-mono text-cyan-400 uppercase tracking-wider font-semibold">Token Optimization</div>
            <div class="bg-white p-4 rounded-2xl border border-slate-200 flex items-center justify-center min-h-[170px] shadow-lg group-hover:scale-[1.02] transition-transform duration-300">
              <img src="{images['vector_compute_logo.jpg']}" alt="Vector Compute Brand Logo" class="max-h-36 max-w-full object-contain">
            </div>
            <h3 class="text-lg font-bold text-slate-100">Vector Compute</h3>
            <p class="text-xs text-slate-400 leading-relaxed">AI LLM Token Logistics & EvoMax Performance Optimization.</p>
          </div>
          <div class="mt-4 pt-3 border-t border-slate-800/80 text-[10px] font-mono text-slate-400 uppercase tracking-wider font-semibold">A MEMBER OF VECTOR ONE HOLDINGS</div>
        </div>

        <!-- CARD 3: VECTOR INTELLIGENCE -->
        <div class="glass-panel p-6 rounded-2xl text-center hover:border-emerald-500/50 transition-all duration-300 group flex flex-col justify-between bg-slate-900/80">
          <div class="space-y-4">
            <div class="text-[11px] font-mono text-emerald-400 uppercase tracking-wider font-semibold">Agentic AI & Consulting</div>
            <div class="bg-white p-4 rounded-2xl border border-slate-200 flex items-center justify-center min-h-[170px] shadow-lg group-hover:scale-[1.02] transition-transform duration-300">
              <img src="{images['vector_intelligence_logo.jpg']}" alt="Vector Intelligence Brand Logo" class="max-h-36 max-w-full object-contain">
            </div>
            <h3 class="text-lg font-bold text-slate-100">Vector Intelligence</h3>
            <p class="text-xs text-slate-400 leading-relaxed">Autonomous Agentic AI Deployment & Data Science Strategy.</p>
          </div>
          <div class="mt-4 pt-3 border-t border-slate-800/80 text-[10px] font-mono text-slate-400 uppercase tracking-wider font-semibold">A MEMBER OF VECTOR ONE HOLDINGS</div>
        </div>

        <!-- CARD 4: VECTOR ACADEMY -->
        <div class="glass-panel p-6 rounded-2xl text-center hover:border-indigo-500/50 transition-all duration-300 group flex flex-col justify-between bg-slate-900/80">
          <div class="space-y-4">
            <div class="text-[11px] font-mono text-indigo-400 uppercase tracking-wider font-semibold">Training & Academy</div>
            <div class="bg-white p-4 rounded-2xl border border-slate-200 flex items-center justify-center min-h-[170px] shadow-lg group-hover:scale-[1.02] transition-transform duration-300">
              <img src="{images['vector_academy_logo.jpg']}" alt="Vector Academy Brand Logo" class="max-h-36 max-w-full object-contain">
            </div>
            <h3 class="text-lg font-bold text-slate-100">Vector Academy</h3>
            <p class="text-xs text-slate-400 leading-relaxed">Center for Advanced AI Learning & Executive Talent Development.</p>
          </div>
          <div class="mt-4 pt-3 border-t border-slate-800/80 text-[10px] font-mono text-slate-400 uppercase tracking-wider font-semibold">A MEMBER OF VECTOR ONE HOLDINGS</div>
        </div>

      </div>

      <!-- MASTER BRAND ECOSYSTEM ARCHITECTURE DIAGRAM -->
      <div class="glass-panel p-6 sm:p-8 rounded-3xl text-center border border-slate-800 space-y-6 bg-slate-900/90 shadow-2xl">
        <h3 class="text-sm font-mono text-cyan-400 uppercase tracking-wider">Complete Vector Brand Ecosystem Diagram</h3>
        <div class="bg-white p-4 sm:p-6 rounded-2xl border border-slate-200 shadow-2xl overflow-hidden">
          <img src="{images['vector_brand_ecosystem.jpg']}" alt="Vector Brand Ecosystem Map" class="w-full max-w-5xl mx-auto rounded-xl object-contain">
        </div>
      </div>

    </div>
  </section>'''

# Also update the header logo tag (around line 65) to use the parent logo base64 image!
header_logo_html = f'''      <!-- BRAND LOGO -->
      <a href="#" class="flex items-center space-x-3 group">
        <div class="relative flex items-center justify-center bg-white p-1.5 rounded-xl border border-cyan-400/60 group-hover:border-cyan-400 transition-all duration-300 shadow-lg shadow-cyan-500/20">
          <img src="{images['vector_one_holdings_logo.jpg']}" alt="Vector One Holdings Logo" class="h-10 w-auto object-contain rounded-lg">
          <div class="absolute -top-1 -right-1 w-2.5 h-2.5 bg-cyan-400 rounded-full animate-ping opacity-75"></div>
        </div>
        <div>
          <div class="font-extrabold text-xl tracking-wider text-slate-100 flex items-center">
            VECTOR<span class="text-cyan-400 ml-1">ONE</span>
          </div>
          <div class="text-[10px] font-mono text-cyan-500/80 tracking-widest uppercase">Vector Systems Group</div>
        </div>
      </a>'''

# Replace Brand Ecosystem Section
section_regex = re.compile(r'<!-- VECTOR BRAND ECOSYSTEM & UNIT LOGOS -->.*?<!-- 5-PILLAR OPERATING ECOSYSTEM \(TABBED SHOWCASE\) -->', re.DOTALL)

# Let's find Section bounds
start_str = "<!-- VECTOR BRAND ECOSYSTEM & UNIT LOGOS -->"
end_str = '<section id="pillars"'

if start_str in html_content and end_str in html_content:
    idx1 = html_content.index(start_str)
    idx2 = html_content.index(end_str)
    html_content = html_content[:idx1] + new_brand_ecosystem_html + "\n\n  " + html_content[idx2:]
    print("Replaced Brand Ecosystem section with Base64 embedded logos.")
else:
    print("Warning: could not locate brand ecosystem section markers exact match.")

# Replace header brand logo
header_start = '<!-- BRAND LOGO -->'
header_end = '</nav>'
if header_start in html_content:
    idx_h1 = html_content.index(header_start)
    idx_h2 = html_content.index('<!-- NAV LINKS -->')
    html_content = html_content[:idx_h1] + header_logo_html + "\n\n      " + html_content[idx_h2:]
    print("Replaced Header brand logo with Base64 embedded logo.")

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print("Saved updated index.html successfully.")

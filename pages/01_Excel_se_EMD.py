import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
from io import BytesIO
import zipfile
import re
from utils.branding import apply_custom_css
from utils.navigation import create_breadcrumb, create_back_button

# Page configuration
st.set_page_config(
    page_title="Excel se EMD | PWD Tools Hub",
    page_icon="📊",
    layout="wide"
)

# Apply branding
apply_custom_css()
create_breadcrumb("Excel se EMD")

def sanitize_filename(name: str) -> str:
    safe = re.sub(r"[^A-Za-z0-9._-]+", "_", name.strip())
    return safe[:80] or "receipt"

def build_receipt_html(payee: str, amount_value: float, work: str) -> str:
    # Minimal HTML using the same style/JS structure as static/html/EmdRefund.html
    # Auto-generates the receipt content on load without prompts or auto-print
    html = f"""
<!DOCTYPE html>
<html lang=\"en\">
<head>
  <meta charset=\"UTF-8\" />
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
  <title>Hand Receipt (RPWA 28)</title>
  <style>
    body {{ font-family: sans-serif; margin: 0; }}
    .container {{ width: 100%; max-width: 900px; margin: 20px auto; border: 1px solid #e1e8e3; padding: 24px; box-sizing: border-box; background: #fff; border-radius: 12px; box-shadow: 0 8px 24px rgba(0,0,0,0.08); }}
    .header {{ text-align: center; margin-bottom: 10px; color: #2E8B57; }}
    .details {{ margin-bottom: 1px; }}
    .amount-words {{ font-style: italic; }}
    .signature-area, .offices {{ width: 100%; border-collapse: collapse; margin-top: 20px; }}
    .signature-area td, .signature-area th, .offices td, .offices th {{ border: 1px solid #ccc; padding: 5px; text-align: left; }}
    .offices td, .offices th {{ border-color: #000; word-wrap: break-word; }}
    .input-field {{ border-bottom: 1px dotted #ccc; padding: 3px; width: calc(100% - 10px); display: inline-block; }}
    .bottom-left-box {{ position: relative; border: 2px solid black; padding: 10px; width: 300px; text-align: left; margin-top: 12px; }}
    .bottom-left-box p {{ margin: 3px 0; }}
    .blue-text {{ color: blue; }}
    @media print {{
      @page {{ size: A4 portrait; margin: 0; }}
      body {{ margin: 0; padding: 0; }}
      .container {{ border: none; width: 210mm; min-height: 297mm; margin: 0; padding: 20mm; box-sizing: border-box; }}
      .input-field {{ border: none; }}
    }}
  </style>
</head>
<body>
  <div class=\"container\">
    <div id=\"receipt-content\"></div>
  </div>
  <script>
    function convertNumberToWords(num) {{
      const ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"];
      const tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"];
      const teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"];
      const crore = " Crore ";
      const lakh = " Lakh ";
      const thousand = " Thousand ";
      const hundred = " Hundred ";
      const andWord = " and ";
      if (!num || isNaN(num)) return "Zero";
      num = Math.floor(num);
      let words = "";
      if (Math.floor(num / 10000000)) {{ words += convertNumberToWords(Math.floor(num / 10000000)) + crore; num %= 10000000; }}
      if (Math.floor(num / 100000)) {{ words += convertNumberToWords(Math.floor(num / 100000)) + lakh; num %= 100000; }}
      if (Math.floor(num / 1000)) {{ words += convertNumberToWords(Math.floor(num / 1000)) + thousand; num %= 1000; }}
      if (Math.floor(num / 100)) {{ words += convertNumberToWords(Math.floor(num / 100)) + hundred; num %= 100; }}
      if (num > 0) {{
        if (words !== "") words += andWord;
        if (num < 10) words += ones[num];
        else if (num < 20) words += teens[num - 10];
        else {{ words += tens[Math.floor(num / 10)]; if (num % 10 > 0) words += " " + ones[num % 10]; }}
      }}
      return words;
    }}
    function generateReceiptHTML(payee, amount, work) {{
      const amountInWords = convertNumberToWords(parseFloat(amount));
      return `
        <div class="header">
          <h2>Payable to: - ${'{'}payee{'}'} ( Electric Contractor)</h2>
          <h2>HAND RECEIPT (RPWA 28)</h2>
          <p>(Referred to in PWF&A Rules 418,424,436 & 438)</p>
          <p>Division - PWD Electric Division, Udaipur</p>
        </div>
        <div class="details">
          <p>(1)Cash Book Voucher No. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Date &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</p>
          <p>(2)Cheque No. and Date &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</p>
          <p>(3) Pay for ECS Rs.${'{'}amount{'}'}/- (Rupees <span id="amount-words" class="amount-words">${'{'}amountInWords{'}'} only</span>)</p>
          <p>(4) Paid by me</p>
          <p>(5) Received from The Executive Engineer PWD Electric Division, Udaipur the sum of Rs. ${'{'}amount{'}'}/- (Rupees <span id="amount-words" class="amount-words">${'{'}amountInWords{'}'} only</span>)</p>
          <p> Name of work for which payment is made: <span id="work-name" class="input-field">${'{'}work{'}'}</span></p>
          <p> Chargeable to Head:- 8443 [EMD-Refund] </p>
          <table class="signature-area">
            <tr><td>Witness</td><td>Stamp</td><td>Signature of payee</td></tr>
            <tr><td>Cash Book No. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Page No. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td><td></td><td></td></tr>
          </table>
          <table class="offices">
            <tr><td>For use in the Divisional Office</td><td>For use in the Accountant General's office</td></tr>
            <tr><td>Checked</td><td>Audited/Reviewed</td></tr>
            <tr><td>Accounts Clerk</td><td>DA &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp  Auditor &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp  Supdt. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp  G.O.</td></tr>
          </table>
        </div>
        <div class="bottom-left-box">
          <p class="blue-text"> Passed for Rs. ${'{'}amount{'}'}</p>
          <p class="blue-text"> In Words Rupees: ${'{'}amountInWords{'}'} Only</p>
          <p class="blue-text"> Chargeable to Head:- 8443 [EMD-Refund]</p>
          <div class="seal"><p>Ar.</p><p>D.A.</p><p>E.E.</p></div>
        </div>`;
    }}
    const payee = {payee!r};
    const amount = {amount_value};
    const work = {work!r};
    document.getElementById('receipt-content').innerHTML = generateReceiptHTML(payee, amount, work);
  </script>
</body>
</html>
"""
    return html

def main():
    st.markdown("#### Generate Hand Receipts (RPWA 28) from Excel")
    st.info("Upload an Excel/CSV, map columns, and download receipts. No external dependency.")

    uploaded = st.file_uploader("Upload Excel or CSV", type=["xlsx", "xls", "csv"], accept_multiple_files=False)

    if not uploaded:
        create_back_button()
        return

    # Read data
    df = None
    sheet_name = None
    try:
        if uploaded.name.lower().endswith((".xlsx", ".xls")):
            xls = pd.ExcelFile(uploaded)
            if len(xls.sheet_names) > 1:
                sheet_name = st.selectbox("Select sheet", xls.sheet_names)
            else:
                sheet_name = xls.sheet_names[0]
            df = xls.parse(sheet_name)
        else:
            df = pd.read_csv(uploaded)
    except Exception as e:
        st.error(f"Failed to read file: {e}")
        create_back_button()
        return

    if df is None or df.empty:
        st.warning("No data found in the file.")
        create_back_button()
        return

    st.markdown("##### Preview")
    st.dataframe(df.head(20), use_container_width=True)

    # Guess columns
    cols = list(df.columns.astype(str))
    def guess(patterns):
        for c in cols:
            lc = c.lower()
            if any(p in lc for p in patterns):
                return c
        return None
    default_payee = guess(["payee", "contractor", "name"]) or cols[0]
    default_amount = guess(["amount", "amt", "emd", "value"]) or cols[min(1, len(cols)-1)]
    default_work = guess(["work", "name of work", "work name"]) or cols[min(2, len(cols)-1)]

    st.markdown("##### Map Columns")
    col1, col2, col3 = st.columns(3)
    with col1:
        payee_col = st.selectbox("Payee column", cols, index=cols.index(default_payee) if default_payee in cols else 0)
    with col2:
        amount_col = st.selectbox("Amount column", cols, index=cols.index(default_amount) if default_amount in cols else (1 if len(cols) > 1 else 0))
    with col3:
        work_col = st.selectbox("Work column", cols, index=cols.index(default_work) if default_work in cols else (2 if len(cols) > 2 else 0))

    run = st.button("Generate Receipts", type="primary")

    if not run:
        create_back_button()
        return

    # Build receipt HTMLs
    records = []
    for idx, row in df.iterrows():
        try:
            payee = str(row[payee_col]).strip()
            work = str(row[work_col]).strip()
            amount_raw = row[amount_col]
            if pd.isna(payee) or pd.isna(work) or pd.isna(amount_raw):
                continue
            amount = float(amount_raw)
            html = build_receipt_html(payee, amount, work)
            filename = f"hand_receipt_{sanitize_filename(payee)}_{idx}.html"
            records.append((idx, payee, amount, work, html, filename))
        except Exception:
            continue

    if not records:
        st.warning("No valid rows to generate receipts.")
        create_back_button()
        return

    st.success(f"Generated {len(records)} receipt(s).")

    # Preview first
    preview_idx = st.selectbox("Preview row", [r[0] for r in records], format_func=lambda i: f"Row {i}")
    preview = next(r for r in records if r[0] == preview_idx)
    components.html(preview[4], height=850, scrolling=True)

    # Downloads
    st.markdown("##### Download")
    col_a, col_b = st.columns([1,1])
    with col_a:
        for idx, payee, amount, work, html, filename in records[:20]:
            st.download_button(
                label=f"Download {filename}",
                data=html,
                file_name=filename,
                mime="text/html",
                use_container_width=True,
                key=f"dl_{idx}"
            )
        if len(records) > 20:
            st.caption(f"Showing first 20 downloads. Use ZIP for all {len(records)} receipts.")

    with col_b:
        buf = BytesIO()
        with zipfile.ZipFile(buf, mode="w", compression=zipfile.ZIP_DEFLATED) as zf:
            for _, _, _, _, html, filename in records:
                zf.writestr(filename, html)
        buf.seek(0)
        st.download_button(
            label=f"Download all as ZIP ({len(records)} files)",
            data=buf.getvalue(),
            file_name="hand_receipts.zip",
            mime="application/zip",
            use_container_width=True,
            key="dl_zip"
        )

    # Navigation
    create_back_button()


if __name__ == "__main__":
    main()
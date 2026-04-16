from app.services.rag_service import process_pdf, query_pdf

print("Starting process_pdf...")
process_pdf('uploads/📄 Export Case Study – Fresh Drumstick (India → Malaysia via Air Cargo).pdf')
print("Starting query_pdf...")
context = query_pdf("give short distribution from this pdf")
print("CONTEXT:")
print(context)

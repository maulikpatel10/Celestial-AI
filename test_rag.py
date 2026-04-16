from app.services.rag_service import process_pdf, query_pdf

print("Starting process_pdf...")
process_pdf('uploads/Free Ai Video Creation Guide (a–z Complete Process).pdf')
print("Starting query_pdf...")
context = query_pdf("what is this document about?")
print(context)

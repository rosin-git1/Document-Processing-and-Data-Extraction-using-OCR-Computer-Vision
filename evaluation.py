from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
from ocr_engine import extract_text
from classifier import extract_invoice_fields

# Ground truth (actual values from your PDFs)
ground_truth = {
    "invoice1.png": "1001",
    "invoice2.png": "2045",
    "invoice3.png": "3099"
}

predicted = []
actual = []

for file, true_invoice in ground_truth.items():
    path = f"data/invoices/{file}"
    text = extract_text(path)
    data = extract_invoice_fields(text)

    pred_invoice = data.get("Invoice Number", "0")

    predicted.append(pred_invoice)
    actual.append(true_invoice)

# Convert to binary match (correct / incorrect)
pred_binary = [1 if p == a else 0 for p, a in zip(predicted, actual)]
actual_binary = [1, 1, 1]

print("Accuracy:", accuracy_score(actual_binary, pred_binary))
print("Precision:", precision_score(actual_binary, pred_binary))
print("Recall:", recall_score(actual_binary, pred_binary))
print("F1 Score:", f1_score(actual_binary, pred_binary))
print("Confusion Matrix:\n", confusion_matrix(actual_binary, pred_binary))

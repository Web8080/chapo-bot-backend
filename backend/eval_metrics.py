# eval_metrics.py
import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, classification_report, confusion_matrix

EVAL_LOG = "eval_log.csv"

def evaluate_predictions():
    if not pd.io.common.file_exists(EVAL_LOG):
        print("❌ No evaluation log found.")
        return

    df = pd.read_csv(EVAL_LOG)
    y_true = df["true_intent"]
    y_pred = df["predicted_intent"]

    acc = accuracy_score(y_true, y_pred)
    prec = precision_score(y_true, y_pred, average='macro', zero_division=0)
    rec = recall_score(y_true, y_pred, average='macro', zero_division=0)

    print("📊 Evaluation Report:")
    print(f"✅ Accuracy: {acc * 100:.2f}%")
    print(f"🎯 Precision: {prec:.2f}")
    print(f"🔁 Recall: {rec:.2f}")
    print("\n🧩 Confusion Matrix:")
    print(confusion_matrix(y_true, y_pred))
    print("\n📋 Classification Report:")
    print(classification_report(y_true, y_pred, zero_division=0))

if __name__ == "__main__":
    evaluate_predictions()

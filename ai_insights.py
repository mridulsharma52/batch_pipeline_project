import google.generativeai as genai
import pandas as pd
genai.configure(api_key="AIzaSyBWGjKkdbN7UD5d36AxL56R65gGSkSPdBA")
model = genai.GenerativeModel("gemini-2.0-flash")
def generate_insights(csv_file):
    print("AI INSIGHTS GENERATION STARTED")
    df = pd.read_csv(csv_file)
    summary = "Dataset has " + str(len(df)) + " records and " + str(len(df.columns)) + " columns. Columns: " + str(list(df.columns))
    prompt = "You are a data analyst. Analyze this dataset and give 3 key insights: " + summary
    response = model.generate_content(prompt)
    print("\n===== AI GENERATED INSIGHTS =====")
    print(response.text)
    with open("insights_report.txt", "w") as f:
        f.write(response.text)
    print("\nInsights saved to insights_report.txt")
if __name__ == "__main__":
    generate_insights("raw_data.csv") 
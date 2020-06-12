"""A program to create training data based on medical literature."""

import pandas as pd


def label_steps(dataframe):
    """Label the data according to daily steps."""
    dataframe.Step_labels = dataframe.Step_labels.astype(str)
    for i, j in dataframe.iterrows():
        if j["Steps"] < 7500:
            dataframe.at[i, "Step_labels"] = "LPA"
        if 7500 < j["Steps"] < 1000:
            dataframe.at[i, "Step_labels"] = "MPA"
        if 10000 < j["Steps"] < 12500:
            dataframe.at[i, "Step_labels"] = "HPA"
        if j["Steps"] > 12500:
            dataframe.at[i, "Step_labels"] = "VHPA"
        # print(j["Step_labels"])


def label_minutes_sitting(dataframe):
    """Label the data according to total minutes sitting daily."""
    dataframe.Sitting_labels = dataframe.Sitting_labels.astype(str)
    for i, j in dataframe.iterrows():
        hours_sitting = j["Minutes_sitting"] / 60
        if hours_sitting < 4:
            dataframe.at[i, "Sitting_labels"] = "LRMS"
        if 4 < hours_sitting < 8:
            dataframe.at[i, "Sitting_labels"] = "MRMS"
        if 8 < hours_sitting < 11:
            dataframe.at[i, "Sitting_labels"] = "HRMS"
        if hours_sitting > 11:
            dataframe.at[i, "Sitting_labels"] = "VHRMS"
        # print(j["Sitting_labels"])


def label_physical_activity(dataframe):
    """Label data according to daily physical activity."""
    dataframe.Activity_labels = dataframe.Activity_labels.astype(str)
    # high_risk = "HRCD"
    for i, j in dataframe.iterrows():
        physical_activity = (
            j["Minutes_moderate_activity"] + j["Minutes_intense_activity"]
        )
        if physical_activity <= 15:
            dataframe.at[i, "Activity_labels"] = "HRCD"
        if 15 < physical_activity <= 30:
            dataframe.at[i, "Activity_labels"] = "MRCD"
        if physical_activity > 30:
            dataframe.at[i, "Activity_labels"] = "LRCD"
        # print(j["Activity_labels"])


# def combine_labels(dataframe):
#     # print(dataframe.Activity_labels)
#     # dataframe["Labels"] = dataframe["Steps_labels"].str.cat(dataframe["Sitting_labels"], sep=", ")
#     for i, j in dataframe.iterrows():
#         print(j["Activity_labels"])


if __name__ == "__main__":
    fitbit_data = pd.read_csv("datasetAccess/FitBitData.csv")
    label_steps(fitbit_data)
    label_minutes_sitting(fitbit_data)
    label_physical_activity(fitbit_data)
    print(fitbit_data)
    # combine_labels(fitbit_data)

from __future__ import print_function

import os.path
import requests
import xmltodict


from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]

# The ID and range of a sample spreadsheet.
SPREADSHEET_ID = os.getenv("SPREADSHEET_ID")
RANGE_NAME = "Sheet1!A2:D"


def get_orders():
    """receives data from Google spreadsheet."""
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json",
                SCOPES,
            )
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    try:
        service = build("sheets", "v4", credentials=creds)

        # Call the Sheets API
        sheet = service.spreadsheets()
        result = (
            sheet.values()
            .get(
                spreadsheetId=SPREADSHEET_ID,
                range=RANGE_NAME,
            )
            .execute()
        )
        values = result.get("values", [])

        if not values:
            print("No data found.")
            return

        return values

    except HttpError as err:
        print(err)


def get_dollar_price():
    response = requests.get("http://www.cbr.ru/scripts/XML_daily.asp")
    response.raise_for_status()
    dict_data = xmltodict.parse(response.content)
    dollar_price_string: str = list(
        filter(lambda v: v["@ID"] == "R01235", dict_data["ValCurs"]["Valute"])
    )[0]["Value"]
    return float(dollar_price_string.replace(",", "."))

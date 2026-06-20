import os
import json
import gspread
from datetime import datetime

from google.oauth2.service_account import Credentials

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]

credentials_dict = json.loads(os.getenv("CREDENTIALS_JSON"))

creds = Credentials.from_service_account_info(credentials_dict, scopes=SCOPES)

client = gspread.authorize(creds)

sheet = client.open("Заявки ТАЛАНТО").sheet1


def add_application(
    username,
    telegram_id,
    service,
    trainer,
    name,
    child_name,
    age,
    experience,
    experience_details,
    phone,
    club_reason,
    group_days,
    days,
    time,
    wishes,
):

    sheet.append_row(
        [
            datetime.now().strftime("%d.%m.%Y %H:%M"),
            username,
            telegram_id,
            service,
            trainer,
            name,
            child_name,
            age,
            experience,
            experience_details,
            phone,
            club_reason,
            group_days,
            days,
            time,
            wishes,
        ]
    )

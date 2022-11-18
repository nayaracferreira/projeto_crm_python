from flask import Blueprint, request
from config.database import cursor, connection

agenda_bp = Blueprint("agenda", __name__)
"""
If you do not want bind any account
Only the gpx files in GPX_OUT sync
"""

from config import GPX_FOLDER, JSON_FILE, SQL_FILE

from utils import make_activities_file
from generator import Generator
if __name__ == "__main__":
    generator = Generator(SQL_FILE)
    
    #generator.delete_activity_by_id(1684700624)
    v = generator.get_old_tracks_ids()
    print(v)

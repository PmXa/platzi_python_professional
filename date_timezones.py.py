from datetime import datetime
import pytz

# ---------------------------
# Main function & entry point
# ---------------------------

def run():
    bogota_tz = pytz.timezone("America/Bogota")
    bogota_time = datetime.now(bogota_tz)

    mexico_tz = pytz.timezone("America/Mexico_City")
    mexico_time = datetime.now(mexico_tz)

    caracas_tz = pytz.timezone("America/Caracas")
    caracas_time = datetime.now(caracas_tz)

    print("CDMX:\t\t", mexico_time.strftime("%d/%m/%Y %H:%M"))
    print("Bogotá:\t\t", bogota_time.strftime("%d/%m/%Y %H:%M"))
    print("Caracas:\t", caracas_time.strftime("%d/%m/%Y %H:%M"))

if __name__ == '__main__':
    run()
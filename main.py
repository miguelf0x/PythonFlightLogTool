# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from datetime import date
from prettytable import PrettyTable
import csv

std_logbook_path = ''


class Flight:

    flight_date: date = '1980.01.30'
    departure_airport = '----'
    arrival_airport = '----'
    landings_count = 0
    total_hours = 0.0
    night_hours = 0.0
    instrument_hours = 0.0
    cross_country_hours = 0.0
    tail_number = ''
    aircraft_manufacturer = ''
    aircraft_type = ''

    def __init__(self, flight_date, departure_airport, arrival_airport, landings_count, total_hours, night_hours, instrument_hours, cross_country_hours, tail_number, aircraft_manufacturer, aircraft_type):
        self.flight_date = flight_date
        self.departure_airport = departure_airport
        self.arrival_airport = arrival_airport
        self.landings_count = int(landings_count)
        self.total_hours = float(total_hours)
        self.night_hours = float(night_hours)
        self.instrument_hours = float(instrument_hours)
        self.cross_country_hours = float(cross_country_hours)
        self.tail_number = tail_number
        self.aircraft_manufacturer = aircraft_manufacturer
        self.aircraft_type = aircraft_type

    def get_landings_count(self):
        return self.landings_count

    def get_total_hours(self):
        return self.total_hours

    def get_night_hours(self):
        return self.night_hours

    def get_instrument_hours(self):
        return self.night_hours

    def get_cross_country_hours(self):
        return self.cross_country_hours

    def get_aircraft_type(self):
        return self.aircraft_type

    def get_aircraft_manufacturer(self):
        return self.aircraft_manufacturer

    def get_list_analogue(self):
        return [self.flight_date, self.departure_airport, self.arrival_airport, self.landings_count, self.total_hours, self.night_hours, self.instrument_hours, self.cross_country_hours, self.tail_number, self.aircraft_manufacturer, self.aircraft_type]


def greeter():
    print('PyFlightLogTool by MiguelFox')
    print('  Ver. 0.0.2, (08/02/2022)  ')
    return


def print_load_menu():
    print('Select input method:')
    print('1. Load from original logbook file')
    print('2. Load from formatted (.csv) logbook file')
    return


def print_main_menu():
    print('Select action:')
    print('1. Print logbook')
    print('2. Edit logbook')
    print('3. Calculate stats')
    print('8. Settings')
    print('9. Save and exit')
    print('0. Exit w/o saving')
    return


def print_stat_menu():
    print('Select action:')
    print('1. Calculate landings and total hours by their types')
    print('2. Calculate landings and total hours by aircraft types')
    print('3. Calculate landings and total hours by aircraft manufacturers')
    print('9. Return to main menu')
    return


def print_edit_menu():
    print('Select action:')
    print('1. Edit flight date')
    print('2. Edit departure and arrival')
    print('3. Edit landing count')
    print('4. Edit flight time')
    print('5. Edit tail number')
    print('6. Edit aircraft manufacturer and type')
    print('7. Delete flight from logbook')
    print('9. Return to main menu')
    return


def user_input():
    input_data = input('> ')
    return input_data


def read_settings():
    global std_logbook_path
    try:
        settings_file = open('./settings.txt', 'r')
    except FileNotFoundError:
        open('./settings.txt', 'w').close()
        change_settings()
    else:
        std_logbook_path = settings_file.readline()
        if std_logbook_path == '':
            change_settings()
    return


def change_settings():
    global std_logbook_path
    settings_file = open('./settings.txt', 'w+')
    std_logbook_path = settings_file.readline()
    print('Current original logbook path: '+std_logbook_path)
    print('Please enter full path to original logbook file: ')
    std_logbook_path = user_input()
    settings_file.write(std_logbook_path)
    return


def resolve_aircraft_type(xplane_type):
    match xplane_type:
        case '29_XP11':
            return ['Aero', 'L-29']
        case '29A_XP11':
            return ['Aero', 'L-29']
        case '29S_XP11':
            return ['Aero', 'L-29']
        case '29R_XP11':
            return ['Aero', 'L-29']
        case 'Aerolite_103':
            return ['Aero-Works', 'Aerolite 103']
        case 'a320neo':
            return ['Airbus', 'A320neo']
        case 'A350_xp11':
            return ['Airbus', 'A350-900']
        case 'a321_StdDef':
            return ['Airbus', 'A321']
        case 'a321':
            return ['Airbus', 'A321']
        case 'A340-600_StdDef':
            return ['Airbus', 'A340-600']
        case 'A340-600':
            return ['Airbus', 'A340-600']
        case 'a319_StdDef':
            return ['Airbus', 'A319']
        case 'a319':
            return ['Airbus', 'A319']
        case 'Baron_58':
            return ['Beechcraft', 'Baron 58']
        case 'C90B':
            return ['Beechcraft', 'King Air C90B']
        case '727-200Adv':
            return ['Boeing', '727-200 Advanced']
        case 'B733':
            return ['Boeing', '737-300']
        case 'B38M':
            return ['Boeing', '737-800']
        case 'b738':
            return ['Boeing', '737-800']
        case 'b738_4k':
            return ['Boeing', '737-800']
        case 'FJS_732_TwinJet':
            return ['Boeing', '737-200']
        case '757-200_xp11':
            return ['Boeing', '757-200']
        case '757-300_xp11':
            return ['Boeing', '757-300']
        case 'CRJ200':
            return ['Bombardier', 'CRJ200']
        case 'Cessna_172SP':
            return ['Cessna', '172SP']
        case 'Cessna_172SP_G1000':
            return ['Cessna', '172SP']
        case 'Cessna_172SP_seaplane':
            return ['Cessna', '172SP']
        case 'Car_Centurion':
            return ['Cessna', 'CT210M Centurion II']
        case 'CirrusSF50':
            return ['Cirrus', 'Vision SF50']
        case 'DHC6':
            return ['De Havilland Canada', 'DHC-6 Twin Otter']
        case 'DHC6F':
            return ['De Havilland Canada', 'DHC-6 Twin Otter']
        case 'DHC6T':
            return ['De Havilland Canada', 'DHC-6 Twin Otter']
        case 'DHC6S':
            return ['De Havilland Canada', 'DHC-6 Twin Otter']
        case 'DHC6G1000':
            return ['De Havilland Canada', 'DHC-6 Twin Otter']
        case 'Eclipse_NG':
            return ['Eclipse', '550 NG']
        case 'SR-71':
            return ['Lockheed', 'SR-71 Blackbird']
        case 'Rotate-MD-80-XP11':
            return ['McDonnell Douglas', 'MD-88']
        case 'F-4':
            return ['McDonnell Douglas', 'F-4 Phantom II']
        case 'Orbiter':
            return ['[Multiple]', 'Space Shuttle']
        case 'CONCORDE_FXP':
            return ['Aérospatiale/BAC', 'Concorde']
        case 'avanti':
            return ['Piaggio', 'P.180 Avanti']
        case 'Car_PC12':
            return ['Pilatus', 'PC-12']
        case 'ASK21':
            return ['Schleicher', 'ASK 21']
        case 'S-76C':
            return ['Sikorsky', 'S-76 Spirit']
        case 'L5_Sentinel':
            return ['Stinson', 'L-5 Sentinel']
        case 'tu154':
            return ['Tupolev', 'TU-154M']
        case _:
            return ['Unknown mfr.', 'Unknown type']


def input_from_std_file():
    global std_logbook_path
    read_settings()
    print('Reading from file '+std_logbook_path)
    std_logbook = open(std_logbook_path, 'r')
    flights = []

    num_lines = sum(1 for _ in std_logbook)
    with open(std_logbook_path, 'r') as std_logbook:
        for i in range(num_lines):
            data = std_logbook.readline().split()
            if data[0] != '2':
                continue
            flight_date = int(data[1])
            data[1] = date((2000 + int(str(flight_date)[:2])), int(str(flight_date)[2:4]), int(str(flight_date)[4:6]))
            flight = data[1:10]
            flight[11:12] = resolve_aircraft_type(data[10])
            current_flight = Flight(*flight)
            flights.append(current_flight)
        return flights


def input_from_csv_file():
    print('Please enter full path to .csv file')
    csv_logbook_path = user_input()
    flights = []
    with open(csv_logbook_path, 'r') as csv_logbook:
        reader = csv.reader(csv_logbook, delimiter=',', quotechar='"')
        for row in reader:
            if row:
                flight_date = row[0]
                new_flight_date = flight_date.replace('"', '')
                this_flight_date = new_flight_date.split('/')
                year, month, day = int(this_flight_date[2]), int(this_flight_date[0]), int(this_flight_date[1])
                row[0] = date(year, month, day)
                current_flight = Flight(*row)
                flights.append(current_flight)
    return flights


def print_flights(flights):
    flights_list = []
    for i in range(len(flights)):
        flights_list.append([i+1, *flights[i].get_list_analogue()])
    flights_table = PrettyTable()
    flights_table.field_names = ['#', 'Flight date', 'Dep. ICAO', 'Arr. ICAO', 'LDG #', 'Total hours', 'Night hours', 'IFR hours', 'C/C hours', 'Tailnumber', 'ACF manufacturer', 'ACF type']
    flights_table.add_rows(flights_list)
    flights_table.align = 'c'
    print(flights_table)
    return


def write_to_file(flights):
    print('Enter file name for output:')
    output_path = user_input()
    with open(output_path+'.csv', 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
        rows = []
        for i in range(len(flights)):
            row = flights[i].get_list_analogue()
            row[0] = row[0].strftime('%m/%d/%Y')
            rows.append(row)
        writer.writerows(rows)
        print(rows)
    return


def edit_flights(flights):
    print_flights(flights)
    print('Enter number of flight that would be edited')
    i = int(user_input())
    flight = flights[i-1].get_list_analogue()
    print_edit_menu()
    j = int(user_input())
    match j:
        case 1:
            print('Enter new flight date (YYYY-MM-DD)')
            flight[0] = user_input()
        case 2:
            print('Enter new departure airport code:')
            flight[1] = user_input()
            print('Enter new arrival airport code:')
            flight[2] = user_input()
        case 3:
            print('Enter new landing count:')
            flight[3] = user_input()
        case 4:
            print('Enter new total hours:')
            flight[4] = user_input()
            print('Enter new night hours:')
            flight[5] = user_input()
            print('Enter new instrument hours:')
            flight[6] = user_input()
            print('Enter new cross-country hours:')
            flight[7] = user_input()
        case 5:
            print('Enter new tail number:')
            flight[8] = user_input()
        case 6:
            print('Enter new aircraft manufacturer:')
            flight[9] = user_input()
            print('Enter new aircraft type:')
            flight[10] = user_input()
        case 7:
            print('Are you sure? [y/n]')
            control = user_input()
            if control == 'y' or control == 'Y':
                for k in range(i, len(flights)):
                    flights[k-1] = flights[k]
                flights.pop(k)
                return flights
            else:
                return
        case 9:
            return flights
    new_flight = Flight(*flight)
    flights[i - 1] = new_flight
    return flights


def calculate_total(flights):
    total_hours_sum = night_hours_sum = instrument_hours_sum = cross_country_sum = 0.0
    total_landings = 0
    for i in range(len(flights)):
        total_hours_sum = total_hours_sum + flights[i].get_total_hours()
        night_hours_sum = night_hours_sum + flights[i].get_night_hours()
        instrument_hours_sum = instrument_hours_sum + flights[i].get_instrument_hours()
        cross_country_sum = cross_country_sum + flights[i].get_cross_country_hours()
        total_landings = total_landings + flights[i].get_landings_count()
    hours_table = PrettyTable()
    hours_table.field_names = ['Total hours', 'Total night hours', 'Total IFR hours', 'Total C/C hours', 'Total landings']
    table_info = [str(total_hours_sum.__round__(1)), str(night_hours_sum.__round__(1)), str(instrument_hours_sum.__round__(1)), str(cross_country_sum.__round__(1)), str(total_landings.__round__(1))]
    hours_table.add_row(table_info)
    hours_table.align = 'c'
    print(hours_table)
    return


def calculate_total_by_type(flights):

    aircraft_type_stat = []
    aircraft_type_list = []
    for i in range(len(flights)):
        if not flights[i].get_aircraft_type() in aircraft_type_list:
            aircraft_type_list.append(flights[i].get_aircraft_type())

    for aircraft_type in aircraft_type_list:
        total_hours_sum = night_hours_sum = instrument_hours_sum = cross_country_sum = 0.0
        total_landings = 0
        for i in range(len(flights)):
            if aircraft_type == flights[i].get_aircraft_type():
                total_hours_sum = total_hours_sum + flights[i].get_total_hours()
                night_hours_sum = night_hours_sum + flights[i].get_night_hours()
                instrument_hours_sum = instrument_hours_sum + flights[i].get_instrument_hours()
                cross_country_sum = cross_country_sum + flights[i].get_cross_country_hours()
                total_landings = total_landings + flights[i].get_landings_count()
        aircraft_type_stat.append([aircraft_type, total_hours_sum.__round__(1), night_hours_sum.__round__(1), instrument_hours_sum.__round__(1), cross_country_sum.__round__(1), total_landings])

    type_table = PrettyTable()
    type_table.field_names = ['Aircraft type', 'Total hours', 'Total night hours', 'Total IFR hours', 'Total C/C hours', 'Total landings']
    type_table.add_rows(aircraft_type_stat)
    type_table.align = 'c'
    print(type_table)
    return


def calculate_total_by_manufacturer(flights):

    aircraft_manufacturer_stat = []
    aircraft_manufacturer_list = []
    for i in range(len(flights)):
        if not flights[i].get_aircraft_manufacturer() in aircraft_manufacturer_list:
            aircraft_manufacturer_list.append(flights[i].get_aircraft_manufacturer())

    for aircraft_manufacturer in aircraft_manufacturer_list:
        total_hours_sum = night_hours_sum = instrument_hours_sum = cross_country_sum = 0.0
        total_landings = 0

        for i in range(len(flights)):
            if aircraft_manufacturer == flights[i].get_aircraft_manufacturer():
                total_hours_sum = total_hours_sum + flights[i].get_total_hours()
                night_hours_sum = night_hours_sum + flights[i].get_night_hours()
                instrument_hours_sum = instrument_hours_sum + flights[i].get_instrument_hours()
                cross_country_sum = cross_country_sum + flights[i].get_cross_country_hours()
                total_landings = total_landings + flights[i].get_landings_count()
        aircraft_manufacturer_stat.append([aircraft_manufacturer, total_hours_sum.__round__(1), night_hours_sum.__round__(1), instrument_hours_sum.__round__(1), cross_country_sum.__round__(1), total_landings])

    manufacturer_table = PrettyTable()
    manufacturer_table.field_names = ['Aircraft manufacturer', 'Total hours', 'Total night hours', 'Total IFR hours', 'Total C/C hours', 'Total landings']
    manufacturer_table.add_rows(aircraft_manufacturer_stat)
    manufacturer_table.align = 'c'
    print(manufacturer_table)
    return


def calculate_stats(flights):
    print_stat_menu()
    user_choice = 7
    while user_choice < 9:
        user_choice = int(user_input())
        match user_choice:
            case 1:
                calculate_total(flights)
            case 2:
                calculate_total_by_type(flights)
            case 3:
                calculate_total_by_manufacturer(flights)
            case 9:
                return
    return


def main():
    greeter()
    print_load_menu()
    user_choice = user_input()

    if int(user_choice) == 1:
        flights = input_from_std_file()
    else:
        flights = input_from_csv_file()

    print(str(len(flights)) + ' flights loaded')

    while int(user_choice) < 9:
        print_main_menu()
        user_choice = int(user_input())
        print(user_choice)
        match user_choice:
            case 1:
                print_flights(flights)
            case 2:
                flights = edit_flights(flights)
            case 3:
                calculate_stats(flights)
            case 8:
                change_settings()
            case 9:
                write_to_file(flights)
                return
            case 0:
                return

    return


main()

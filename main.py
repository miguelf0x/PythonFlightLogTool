# PyFlightLogTool made by MiguelFox
# Version 0.1.5, 09.02.2022


from datetime import date
from prettytable import PrettyTable
import csv

std_logbook_path = ''


class AircraftInfo:

    xplane_type = ''
    manufacturer = 'Unknown mfr.'
    aircraft_type = 'Unknown type'
    engines_count = 1
    engines_type = 'Unknown'  # Piston/Turboprop/Turboshaft/Turbojet/Turbofan/Electric/Unknown/None
    aircraft_class = 'Land'  # Land/Seaplane/Amphibian

    def __init__(self, xplane_type, manufacturer, aircraft_type, engines_count, engines_type='Unknown',
                 aircraft_class='Land'):
        self.xplane_type = xplane_type
        self.manufacturer = manufacturer
        self.aircraft_type = aircraft_type
        self.engines_count = int(engines_count)
        self.engines_type = engines_type
        self.aircraft_class = aircraft_class

    def set_xplane_type(self, xplane_type):
        self.xplane_type = xplane_type

    def set_aircraft_manufacturer(self, manufacturer):
        self.manufacturer = manufacturer

    def set_aircraft_type(self, acf_type):
        self.aircraft_type = acf_type

    def set_engines_count(self, engines_count):
        self.engines_count = engines_count

    def set_engines_type(self, engines_type):
        self.engines_type = engines_type

    def set_aircraft_class(self, acf_class):
        self.aircraft_class = acf_class

    def get_xplane_type(self):
        return self.xplane_type

    def get_aircraft_type(self):
        return self.aircraft_type

    def get_aircraft_manufacturer(self):
        return self.manufacturer

    def get_engines_count(self):
        return self.engines_count

    def get_engines_type(self):
        return self.engines_type

    def get_aircraft_class(self):
        return self.aircraft_class

    def get_full_info(self):
        return [self.xplane_type, self.manufacturer, self.aircraft_type, self.engines_count, self.engines_type,
                self.aircraft_class]

    def get_resolved_info(self):
        return [self.manufacturer, self.aircraft_type, self.engines_count, self.engines_type, self.aircraft_class]


class Flight:

    flight_date: date
    departure_airport = '----'
    arrival_airport = '----'
    landings_count = 0
    total_hours = 0.0
    night_hours = 0.0
    instrument_hours = 0.0
    cross_country_hours = 0.0
    tailnumber = ''
    aircraft: AircraftInfo

    def __init__(self, flight_date, departure_airport, arrival_airport, landings_count, total_hours, night_hours,
                 instrument_hours, cross_country_hours, tailnumber, aircraft):
        self.flight_date = flight_date
        self.departure_airport = departure_airport
        self.arrival_airport = arrival_airport
        self.landings_count = int(landings_count)
        self.total_hours = float(total_hours)
        self.night_hours = float(night_hours)
        self.instrument_hours = float(instrument_hours)
        self.cross_country_hours = float(cross_country_hours)
        self.tailnumber = tailnumber
        self.aircraft: AircraftInfo = aircraft

    def set_flight_date(self, flight_date):
        this_flight_date = flight_date.split('/')
        self.flight_date = date(int(this_flight_date[0]), int(this_flight_date[1]), int(this_flight_date[2]))

    def set_airports(self, departure_airport, arrival_airport):
        self.departure_airport = departure_airport
        self.arrival_airport = arrival_airport

    def set_landings_count(self, landings_count):
        self.landings_count = landings_count

    def set_flight_hours(self, total_hours, night_hours, instrument_hours, cross_country_hours):
        self.total_hours = total_hours
        self.night_hours = night_hours
        self.instrument_hours = instrument_hours
        self.cross_country_hours = cross_country_hours

    def set_tailnumber(self, tailnumber):
        self.tailnumber = tailnumber

    def set_aircraft_manufacturer(self, manufacturer):
        self.aircraft.manufacturer = manufacturer

    def set_aircraft_type(self, acf_type):
        self.aircraft.aircraft_type = acf_type

    def set_engine_count(self, engine_count):
        self.aircraft.engines_count = engine_count

    def set_engine_type(self, engine_type):
        self.aircraft.engines_type = engine_type

    def set_aircraft_class(self, acf_class):
        self.aircraft.aircraft_class = acf_class

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

    def get_hours_and_landings(self):
        return [self.total_hours.__round__(1), self.night_hours.__round__(1), self.instrument_hours.__round__(1),
                self.cross_country_hours.__round__(1), self.landings_count]

    def get_aircraft_tailnumber(self):
        return self.tailnumber

    def get_aircraft_type(self):
        return self.aircraft.get_aircraft_type()

    def get_aircraft_manufacturer(self):
        return self.aircraft.get_aircraft_manufacturer()

    def get_engines_count(self):
        return self.aircraft.get_engines_count()

    def get_engines_type(self):
        return self.aircraft.get_engines_type()

    def get_aircraft_class(self):
        return self.aircraft.get_aircraft_class()

    def get_list_analogue(self):
        return [self.flight_date, self.departure_airport, self.arrival_airport, self.landings_count, self.total_hours,
                self.night_hours, self.instrument_hours, self.cross_country_hours, self.tailnumber,
                *self.aircraft.get_resolved_info()]

    def get_full_list_analogue(self):
        return [self.flight_date, self.departure_airport, self.arrival_airport, self.landings_count, self.total_hours,
                self.night_hours, self.instrument_hours, self.cross_country_hours, self.tailnumber,
                *self.aircraft.get_full_info()]


greeter = ['PyFlightLogTool by MiguelFox',
           'Ver. 0.1.5, 09/02/2022']
load_menu = ['Select input method:',
             '1. Load from original logbook file',
             '2. Load from formatted (.csv) logbook file']
main_menu = ['Select action:',
             '1. Print logbook',
             '2. Edit logbook',
             '3. Calculate stats',
             '7. Aircraft types',
             '8. Settings',
             '9. Save and exit',
             '0. Exit w/o saving']
stat_menu = ['Select action:',
             '1. Calculate landings and total hours by their types',
             '2. Calculate landings and total hours by aircraft types',
             '3. Calculate landings and total hours by aircraft manufacturers',
             '4. Calculate landings and total hours by engines count',
             '5. Calculate landings and total hours by engines type',
             '6. Calculate landings and total hours by aircraft class',
             '9. Return to main menu']
types_menu = ['Select action:',
              '1. Print known type references',
              '2. Add type reference',
              '3. Remove type reference',
              '7. Load types config',
              '8. Write types config',
              '9. Return to main menu']
edit_menu = ['Select action:',
             '1. Edit flight date',
             '2. Edit departure and arrival',
             '3. Edit landing count',
             '4. Edit flight time',
             '5. Edit tail number',
             '6. Edit aircraft info',
             '7. Delete flight from logbook',
             '9. Return to main menu']
class_menu = ['Select aircraft class:',
              '1. Land',
              '2. Seaplane',
              '3. Amphibian']


def print_menu(menu):
    for i in menu:
        print(i)


def user_input():
    input_data = input('> ')
    try:
        new_input_data = int(input_data)
    except TypeError:
        return input_data
    except ValueError:
        return input_data
    else:
        return new_input_data


def read_settings():
    global std_logbook_path
    try:
        settings_file = open('./config/settings.txt', 'r')
    except FileNotFoundError:
        open('./config/settings.txt', 'w').close()
        change_settings()
    else:
        std_logbook_path = settings_file.readline()
        if std_logbook_path == '':
            change_settings()
    return


def change_settings():
    global std_logbook_path
    settings_file = open('./config/settings.txt', 'w+')
    std_logbook_path = settings_file.readline()
    if std_logbook_path == '':
        std_logbook_path = 'None specified'
    print('Current original logbook path: '+std_logbook_path)
    print('Please enter full path to original logbook file:')
    std_logbook_path = user_input()
    settings_file.write(std_logbook_path)
    return


def resolve_aircraft_type(xplane_type, acf_types):
    for i in range(len(acf_types)):
        if xplane_type == acf_types[i].get_xplane_type():
            return acf_types[i]
    unknown_aircraft = AircraftInfo(xplane_type, 'Unknown mfr.', xplane_type, 0, 'Unknown', 'Land')
    return unknown_aircraft


def input_from_std_file(acf_types):
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
            # noinspection PyTypeChecker
            data[1] = date((2000 + int(str(flight_date)[:2])), int(str(flight_date)[2:4]), int(str(flight_date)[4:6]))
            flight = data[1:10]
            current_flight = Flight(*flight, resolve_aircraft_type(data[10], acf_types))
            flights.append(current_flight)
        return flights


def input_from_csv_file():
    print('Please enter full path to .csv file')
    csv_logbook_path = user_input()
    if csv_logbook_path[(len(csv_logbook_path)-4):] != '.csv':
        csv_logbook_path += '.csv'
    flights = []
    with open(csv_logbook_path, 'r') as csv_logbook:
        reader = csv.reader(csv_logbook, delimiter=',', quotechar='"')
        for row in reader:
            if row:
                flight_date = row[0]
                new_flight_date = flight_date.replace('"', '')
                this_flight_date = new_flight_date.split('/')
                year, month, day = int(this_flight_date[2]), int(this_flight_date[0]), int(this_flight_date[1])
                # noinspection PyTypeChecker
                row[0] = date(year, month, day)
                current_flight = Flight(*row[0:9], AircraftInfo(*row[9:15]))
                flights.append(current_flight)
    return flights


def print_flights(flights):
    flights_list = []
    for i in range(len(flights)):
        flights_list.append([i + 1, *flights[i].get_list_analogue()])
    flights_table = PrettyTable()
    flights_table.field_names = ['#', 'Flight date', 'Dep. ICAO', 'Arr. ICAO', 'LDG #', 'Total hours', 'Night hours',
                                 'IFR hours', 'C/C hours', 'Tailnumber', 'ACF manufacturer', 'ACF type', 'ENG #',
                                 'ENG type', 'ACF class']
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
            row = flights[i].get_full_list_analogue()
            row[0] = row[0].strftime('%m/%d/%Y')
            rows.append(row)
        writer.writerows(rows)
    return


def edit_flights(flights):
    print_flights(flights)
    print('Enter number of flight that would be edited:')
    i = user_input()
    while i < 0 or i > len(flights):
        print('Flight number out of range! Enter correct number:')
        i = user_input()
    flight = flights[i-1]

    print_menu(edit_menu)
    j = 8
    while j != 0:
        j = user_input()
        match j:
            case 1:
                print('Enter new flight date (YYYY/MM/DD)')
                flight.set_flight_date(user_input())
            case 2:
                print('Enter new departure airport code:')
                airports = ['', '']
                airports[1] = user_input()
                print('Enter new arrival airport code:')
                airports[2] = user_input()
                flight.set_airports(*airports)
            case 3:
                print('Enter landings count:')
                flight.set_landings_count(user_input())
            case 4:
                flight_hours = [0.0, 0.0, 0.0, 0.0]
                print('Enter new total hours:')
                flight_hours[0] = user_input()
                print('Enter new night hours:')
                flight_hours[1] = user_input()
                print('Enter new instrument hours:')
                flight_hours[2] = user_input()
                print('Enter new cross-country hours:')
                flight_hours[3] = user_input()
                flight.set_flight_hours(*flight_hours)
            case 5:
                print('Enter new tailnumber (current: ' + flight.get_aircraft_tailnumber() + '):')
                flight.set_tailnumber(user_input())
            case 6:
                print('Enter new aircraft manufacturer (current:' + flight.get_aircraft_manufacturer() + '):')
                flight.set_aircraft_manufacturer(user_input())
                print('Enter new aircraft type (current:' + flight.get_aircraft_type() + '):')
                flight.set_aircraft_type(user_input())
                print('Enter new engine count (current:' + str(flight.get_engines_count()) + '):')
                flight.set_engines_count(user_input())
                print('Enter new engine type (current:' + str(flight.get_engines_type()) + '):')
                flight.set_engine_type(user_input())
                print('Select new aircraft class (current:' + flight.get_aircraft_class() + '):')
                print_menu(class_menu)
                acf_class = user_input()
                new_class = 'Land'
                match acf_class:
                    case 2:
                        new_class = 'Seaplane'
                    case 3:
                        new_class = 'Amphibian'
                flight.set_aircraft_class(new_class)
            case 7:
                print('Are you sure? [y/n]')
                control = user_input()
                if control == 'y' or control == 'Y':
                    k = i
                    for k in range(i, len(flights)):
                        flights[k-1] = flights[k]
                    flights.pop(k)
                    return flights
                else:
                    return
            case 8:
                pass
            case 9:
                return flights
            case _:
                print('Menu entry number out of range! Enter correct number:')

    flights[i - 1] = flight
    return flights


def calculate_total(flights):
    total_hours_sum = night_hours_sum = instrument_hours_sum = cross_country_sum = 0.0
    total_landings = 0
    for i in range(len(flights)):
        total_hours_sum += flights[i].get_total_hours()
        night_hours_sum += flights[i].get_night_hours()
        instrument_hours_sum += flights[i].get_instrument_hours()
        cross_country_sum += flights[i].get_cross_country_hours()
        total_landings += flights[i].get_landings_count()

    hours_table = PrettyTable()
    hours_table.field_names = ['Total hours', 'Total night hours', 'Total IFR hours', 'Total C/C hours',
                               'Total landings']
    table_info = [str(total_hours_sum.__round__(1)), str(night_hours_sum.__round__(1)),
                  str(instrument_hours_sum.__round__(1)), str(cross_country_sum.__round__(1)),
                  str(total_landings.__round__(1))]
    hours_table.add_row(table_info)
    hours_table.align = 'c'
    print(hours_table)
    return


def calculate_total_by_type(flights):
    sum_hours(flights, "get_aircraft_type", ['Aircraft type', 'Total hours', 'Total night hours', 'Total IFR hours',
                                             'Total C/C hours', 'Total landings'])
    return


def calculate_total_by_manufacturer(flights):
    sum_hours(flights, "get_aircraft_manufacturer", ['Aircraft manufacturer', 'Total hours', 'Total night hours',
                                                     'Total IFR hours', 'Total C/C hours', 'Total landings'])
    return


def calculate_total_by_engine_count(flights):
    sum_hours(flights, "get_engines_count", ['Engines count', 'Total hours', 'Total night hours', 'Total IFR hours',
                                             'Total C/C hours', 'Total landings'])
    return


def calculate_total_by_engine_type(flights):
    sum_hours(flights, "get_engines_type", ['Engines type', 'Total hours', 'Total night hours', 'Total IFR hours',
                                            'Total C/C hours', 'Total landings'])
    return


def calculate_total_by_aircraft_class(flights):
    sum_hours(flights, "get_aircraft_class", ['Aircraft class', 'Total hours', 'Total night hours', 'Total IFR hours',
                                              'Total C/C hours', 'Total landings'])
    return


def sum_hours(flights, method, field_names):
    info_stat = []
    info_list = []
    for i in range(len(flights)):
        condition = getattr(flights[i], method)()
        if condition in info_list:
            n = info_list.index(condition)
            for j in range(1, 4):
                info_stat[n][j] += flights[i].get_hours_and_landings()[j-1]
                info_stat[n][j] = info_stat[n][j].__round__(1)
            info_stat[n][5] += flights[i].get_hours_and_landings()[4]
        else:
            info_list.append(condition)
            info_stat.append([condition, *flights[i].get_hours_and_landings()])

    info_stat.sort()
    draw_table(field_names, info_stat)
    return


def draw_table(field_names, rows):
    table = PrettyTable()
    table.field_names = field_names
    table.add_rows(rows)
    table.align = 'c'
    print(table)


def calculate_stats(flights):
    user_choice = 7
    while user_choice < 9:
        print_menu(stat_menu)
        user_choice = user_input()
        match user_choice:
            case 1:
                calculate_total(flights)
            case 2:
                calculate_total_by_type(flights)
            case 3:
                calculate_total_by_manufacturer(flights)
            case 4:
                calculate_total_by_engine_count(flights)
            case 5:
                calculate_total_by_engine_type(flights)
            case 6:
                calculate_total_by_aircraft_class(flights)
            case 9:
                return
    return


def load_type_reference():
    acf_types = []
    with open('./config/acf_types_table.csv', 'r') as acf_types_table:
        reader = csv.reader(acf_types_table, delimiter=',', quotechar='"')
        for row in reader:
            if row:
                acf_type = AircraftInfo(*row)
                acf_types.append(acf_type)
    return acf_types


def write_type_reference(acf_types):
    with open('./config/acf_types_table.csv', 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
        rows = []
        for i in range(len(acf_types)):
            row = acf_types[i].get_full_info()
            rows.append(row)
        writer.writerows(rows)
    return


def add_type_reference(acf_types):
    acf_type = ['', '', '', 1, '']

    print('Enter X-Plane 11 type:')
    acf_type[0] = user_input()
    print('Enter aircraft manufacturer:')
    acf_type[1] = user_input()
    print('Enter aircraft type:')
    acf_type[2] = user_input()
    print('Enter engine count:')
    acf_type[3] = user_input()
    print('Enter engine type:')
    acf_type[4] = user_input()

    # Land/Seaplane/Amphibian
    print_menu(class_menu)
    acf_class = user_input()
    acf_type[5] = 'Land'
    match acf_class:
        case 2:
            acf_type[5] = 'Seaplane'
        case 3:
            acf_type[5] = 'Amphibian'

    new_acf_type = AircraftInfo(*acf_type)
    acf_types.append(new_acf_type)

    return acf_types


def rm_type_reference(acf_types):
    print_acf_types(acf_types)
    print('Select # of type that will be deleted')
    i = user_input()
    print('Are you sure? [Y/N]')
    acknowledge = user_input()
    if acknowledge == 'y' or acknowledge == 'Y':
        j = i
        for j in range(j, len(acf_types)):
            acf_types[j-1] = acf_types[j]
        acf_types.pop(j)
    return acf_types


def print_acf_types(acf_types):
    acf_types_list = []
    for i in range(len(acf_types)):
        acf_types_list.append([i + 1, *acf_types[i].get_full_info()])
    types_table = PrettyTable()
    types_table.field_names = ['#', 'X-Plane type', 'ACF manufacturer', 'ACF type', 'ENG #', 'ENG type', 'ACF class']
    types_table.add_rows(acf_types_list)
    types_table.align = 'c'
    print(types_table)


def acf_types_menu(acf_types):
    user_choice = 1
    while user_choice != 9:
        match user_choice:
            case 1:
                print_acf_types(acf_types)
            case 2:
                acf_types = add_type_reference(acf_types)
            case 3:
                acf_types = rm_type_reference(acf_types)
            case 7:
                acf_types = load_type_reference()
            case 8:
                write_type_reference(acf_types)
        print_menu(types_menu)
        user_choice = user_input()

    return acf_types


def main():
    print_menu(greeter)
    print_menu(load_menu)

    acf_types = load_type_reference()

    user_choice = user_input()
    while type(user_choice) != int:
        print('Please enter menu entry number:')
        user_choice = user_input()

    while user_choice < 0 or user_choice > 2:
        print('Menu entry number out of range! Enter correct number:')
        user_choice = user_input()

    if user_choice == 1:
        flights = input_from_std_file(acf_types)
    else:
        flights = input_from_csv_file()

    print(str(len(flights)) + ' flights loaded')

    while user_choice < 9:
        print_menu(main_menu)
        user_choice = user_input()
        match user_choice:
            case 1:
                print_flights(flights)
            case 2:
                flights = edit_flights(flights)
            case 3:
                calculate_stats(flights)
            case 7:
                acf_types = acf_types_menu(acf_types)
            case 8:
                change_settings()
            case 9:
                write_to_file(flights)
                return
            case 0:
                return

    return


main()

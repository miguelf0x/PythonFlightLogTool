# PyFlightLogTool made by MiguelFox
# Version 0.1.1, 09.02.2022


from datetime import date
from prettytable import PrettyTable
import csv

std_logbook_path = ''


class AircraftInfo:

    xplane_type = ''
    manufacturer = 'Unknown mfr.'
    acf_type = 'Unknown type'
    engine_count = 1
    acf_class = 'Land'  # Land/Seaplane/Amphibian

    def __init__(self, xplane_type, manufacturer, acf_type, engine_count, acf_class):
        self.xplane_type = xplane_type
        self.manufacturer = manufacturer
        self.acf_type = acf_type
        self.engine_count = int(engine_count)
        self.acf_class = acf_class

    def set_xplane_type(self, xplane_type):
        self.xplane_type = xplane_type

    def set_aircraft_manufacturer(self, manufacturer):
        self.manufacturer = manufacturer

    def set_aircraft_type(self, acf_type):
        self.acf_type = acf_type

    def set_engine_count(self, engine_count):
        self.engine_count = engine_count

    def set_aircraft_class(self, acf_class):
        self.acf_class = acf_class

    def get_xplane_type(self):
        return self.xplane_type

    def get_aircraft_type(self):
        return self.acf_type

    def get_aircraft_manufacturer(self):
        return self.manufacturer

    def get_engine_count(self):
        return self.engine_count

    def get_aircraft_class(self):
        return self.acf_class

    def get_list_analogue(self):
        return [self.xplane_type, self.manufacturer, self.acf_type, self.engine_count, self.acf_class]

    def get_resolved_info(self):
        return [self.manufacturer, self.acf_type, self.engine_count, self.acf_class]


class Flight:

    flight_date: date
    departure_airport = '----'
    arrival_airport = '----'
    landings_count = 0
    total_hours = 0.0
    night_hours = 0.0
    instrument_hours = 0.0
    cross_country_hours = 0.0
    tail_number = ''
    aircraft: AircraftInfo

    def __init__(self, flight_date, departure_airport, arrival_airport, landings_count, total_hours, night_hours,
                 instrument_hours, cross_country_hours, tail_number, aircraft):
        self.flight_date = flight_date
        self.departure_airport = departure_airport
        self.arrival_airport = arrival_airport
        self.landings_count = int(landings_count)
        self.total_hours = float(total_hours)
        self.night_hours = float(night_hours)
        self.instrument_hours = float(instrument_hours)
        self.cross_country_hours = float(cross_country_hours)
        self.tail_number = tail_number
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
        self.tail_number = tailnumber

    def set_aircraft_manufacturer(self, manufacturer):
        self.aircraft.manufacturer = manufacturer

    def set_aircraft_type(self, acf_type):
        self.aircraft.acf_type = acf_type

    def set_engine_count(self, engine_count):
        self.aircraft.engine_count = engine_count

    def set_aircraft_class(self, acf_class):
        self.aircraft.acf_class = acf_class

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

    def get_aircraft_tailnumber(self):
        return self.tail_number

    def get_aircraft_type(self):
        return self.aircraft.get_aircraft_type()

    def get_aircraft_manufacturer(self):
        return self.aircraft.get_aircraft_manufacturer()

    def get_engine_count(self):
        return self.aircraft.get_engine_count()

    def get_aircraft_class(self):
        return self.aircraft.get_aircraft_class()

    def get_list_analogue(self):
        return [self.flight_date, self.departure_airport, self.arrival_airport, self.landings_count, self.total_hours,
                self.night_hours, self.instrument_hours, self.cross_country_hours, self.tail_number,
                *self.aircraft.get_resolved_info()]

    def get_full_list_analogue(self):
        return [self.flight_date, self.departure_airport, self.arrival_airport, self.landings_count, self.total_hours,
                self.night_hours, self.instrument_hours, self.cross_country_hours, self.tail_number,
                *self.aircraft.get_list_analogue()]


def greeter():
    print('PyFlightLogTool by MiguelFox')
    print('  Ver. 0.1.1, (09/02/2022)  ')
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
    print('7. Aircraft types')
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


def print_types_menu():
    print('Select action:')
    print('1. Print known type references')
    print('2. Add type reference')
    print('3. Remove type reference')
    print('7. Load types config')
    print('8. Write types config')
    print('9. Return to main menu')
    return


def print_edit_menu():
    print('Select action:')
    print('1. Edit flight date')
    print('2. Edit departure and arrival')
    print('3. Edit landing count')
    print('4. Edit flight time')
    print('5. Edit tail number')
    print('6. Edit aircraft info')
    print('7. Delete flight from logbook')
    print('9. Return to main menu')
    return


def print_class_menu():
    print('Select aircraft class:')
    print('1. Land')
    print('2. Seaplane')
    print('3. Amphibian')


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
        open('./settings.txt', 'w').close()
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
    unknown_aircraft = AircraftInfo(xplane_type, 'Unknown mfr.', 'Unknown type', 0, 'Land')
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
            data[1] = date((2000 + int(str(flight_date)[:2])), int(str(flight_date)[2:4]), int(str(flight_date)[4:6]))
            flight = data[1:10]
            current_flight = Flight(*flight, resolve_aircraft_type(data[10], acf_types))
            flights.append(current_flight)
        return flights


def input_from_csv_file(acf_types):
    print('Please enter full path to .csv file')
    csv_logbook_path = user_input()
    print(csv_logbook_path[:-4])
    if csv_logbook_path[:-4] != '.csv':
        pass
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
                current_flight = Flight(*row[0:9], AircraftInfo(*row[9:14]))
                flights.append(current_flight)
    return flights


def print_flights(flights):
    flights_list = []
    for i in range(len(flights)):
        flights_list.append([i+1, *flights[i].get_list_analogue()])
    flights_table = PrettyTable()
    flights_table.field_names = ['#', 'Flight date', 'Dep. ICAO', 'Arr. ICAO', 'LDG #', 'Total hours', 'Night hours',
                                 'IFR hours', 'C/C hours', 'Tailnumber', 'ACF manufacturer', 'ACF type', 'ENG #',
                                 'ACF class']
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
    print_edit_menu()
    j = user_input()
    while j < 0 or j > 9:
        print('Menu entry number out of range! Enter correct number:')
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
            print('Enter new engine count (current:' + str(flight.get_engine_count()) + '):')
            flight.set_engine_count(user_input())
            print('Select new aircraft class (current:' + flight.get_aircraft_class() + '):')
            print_class_menu()
            acf_class = user_input()
            match acf_class:
                case 1:
                    new_class = 'Land'
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
        case 9:
            return flights
        case _:
            return flights

    flights[i - 1] = flight
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
        aircraft_type_stat.append([aircraft_type, total_hours_sum.__round__(1), night_hours_sum.__round__(1),
                                   instrument_hours_sum.__round__(1), cross_country_sum.__round__(1), total_landings])

    type_table = PrettyTable()
    type_table.field_names = ['Aircraft type', 'Total hours', 'Total night hours', 'Total IFR hours', 'Total C/C hours',
                              'Total landings']
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
        aircraft_manufacturer_stat.append([aircraft_manufacturer, total_hours_sum.__round__(1),
                                           night_hours_sum.__round__(1), instrument_hours_sum.__round__(1),
                                           cross_country_sum.__round__(1), total_landings])

    manufacturer_table = PrettyTable()
    manufacturer_table.field_names = ['Aircraft manufacturer', 'Total hours', 'Total night hours', 'Total IFR hours',
                                      'Total C/C hours', 'Total landings']
    manufacturer_table.add_rows(aircraft_manufacturer_stat)
    manufacturer_table.align = 'c'
    print(manufacturer_table)
    return


def calculate_stats(flights):
    print_stat_menu()
    user_choice = 7
    while user_choice < 9:
        user_choice = user_input()
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
            row = acf_types[i].get_list_analogue()
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
    print('Enter engines count:')
    acf_type[3] = user_input()

    # Land/Seaplane/Amphibian
    print_class_menu()
    acf_class = user_input()
    match acf_class:
        case 1:
            acf_type[4] = 'Land'
        case 2:
            acf_type[4] = 'Seaplane'
        case 3:
            acf_type[4] = 'Amphibian'

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
        acf_types_list.append([i+1, *acf_types[i].get_list_analogue()])
    types_table = PrettyTable()
    types_table.field_names = ['#', 'X-Plane type', 'ACF manufacturer', 'ACF type', 'ENG #', 'ACF class']
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
        print_types_menu()
        user_choice = user_input()

    return acf_types


def main():
    greeter()
    print_load_menu()

    acf_types = load_type_reference()

    user_choice = user_input()
    if user_choice == 1:
        flights = input_from_std_file(acf_types)
    else:
        flights = input_from_csv_file(acf_types)

    print(str(len(flights)) + ' flights loaded')

    while user_choice < 9:
        print_main_menu()
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

"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*wagons):
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    *wagons_list, = wagons
    return wagons_list


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    :param each_wagons_id: list - the list of wagons.
    :param missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    combined_list = [each_wagons_id, missing_wagons]
    [[first, second, third, *rest], missing] = combined_list

    # Put them in order.
    final_list = [third, *missing, *rest, first, second]
    return final_list


def add_missing_stops(route, **stop_number):
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    *stops, = stop_number.values()

    route['stops'] = stops
    return route


def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    consolidated_dict = {**route, **more_route_information}
    return consolidated_dict


def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """
    [[first_1, second_1, third_1], [first_2, second_2, third_2], [first_3, second_3, third_3]] = wagons_rows

    final_list = [[first_1, first_2, first_3],
             [second_1, second_2, second_3],
             [third_1, third_2, third_3]]
    return final_list
    
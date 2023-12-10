# day05_1.py
import re

seeds = []
gardening_maps = {}


def get_seeds_and_maps(filename: str):
    with open(filename, mode='r') as f:
        global gardening_maps
        current_funnel = []
        for line in f:
            if line.startswith('seeds'):
                global seeds
                seeds = list(map(int, re.findall(r'\d+', line)))
            elif result := re.match(r'([\w-]+)(?= map:)', line):
                if current_funnel:
                    gardening_maps[current_map] = current_funnel

                current_map = result.group(1)
                current_funnel = []
                pass
            elif result := re.findall(r'\d+', line):
                destination_start, source_start, range_length = result
                current_funnel.append({
                    'destination_start': int(destination_start),
                    'source_start': int(source_start),
                    'length': int(range_length)
                })
        gardening_maps[current_map] = current_funnel


def find_soil_for_seed(seed: int) -> int:
    return find_destination_for_source('seed-to-soil', seed)


def find_fertilizer_for_soil(soil: int) -> int:
    return find_destination_for_source('soil-to-fertilizer', soil)


def find_water_for_fertilizer(fertilizer: int) -> int:
    return find_destination_for_source('fertilizer-to-water', fertilizer)


def find_light_for_water(water: int) -> int:
    return find_destination_for_source('water-to-light', water)


def find_temperature_for_light(light: int) -> int:
    return find_destination_for_source('light-to-temperature', light)


def find_humidity_for_temperature(temperature: int) -> int:
    return find_destination_for_source('temperature-to-humidity', temperature)


def find_location_for_humidity(humidity: int) -> int:
    return find_destination_for_source('humidity-to-location', humidity)


def find_destination_for_source(map_name: str, source_value: int) -> int:
    destination = source_value
    for funnel in gardening_maps[map_name]:
        if source_value in range(funnel['source_start'], funnel['source_start'] + funnel['length']):
            destination = (source_value - funnel['source_start']) + funnel['destination_start']
            break
    return destination


def find_lowest_location() -> int:
    seed_location_pairs = []
    for seed_pick in seeds:
        loc = find_location_for_humidity(find_humidity_for_temperature(find_temperature_for_light(
            find_light_for_water(find_water_for_fertilizer(find_fertilizer_for_soil(find_soil_for_seed(seed_pick)))))))
        seed_location_pairs.append({'seed': seed_pick, 'location': loc})
    return min([pair['location'] for pair in seed_location_pairs])


if __name__ == "__main__":
    get_seeds_and_maps('input')
    print(find_lowest_location())

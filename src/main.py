import os
from typing import List 

import segno

import argparse
import uuid

from constants import TDL_LIST

def get_names_from_file(filename: str):
    with open(filename, 'r') as f:
        names = f.read().splitlines()
        return names

def save_qr_code(name, uuid, event_id=None, domain='com', qr_directory=".", custom_name=None, **kwargs):
    qr_code = segno.make(f'https://www.eventbrite.{domain}/e/{event_id}/?discount={uuid}')
    
    if custom_name:
        name = f"{custom_name}-{name}"

    qr_code.save(f'{qr_directory}/{name}.png')

def write_promo_code(names: List[str], qr=False, output_file="code.csv", **kwargs):
    with open(output_file, 'w') as f:
        for name in names:
            uuid_str = str(uuid.uuid4())
            f.write(uuid_str + '\n')
            if qr:
                save_qr_code(name, uuid_str, **kwargs)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
                    prog='code-generator',
                    description='Generate promo codes for Eventbrite events and save them to a file.',
    )
    parser.add_argument('-c', '--count', dest='count', help='File containing names of the attendees.', type=int, default=None)
    parser.add_argument('--filename', required=True, help='File containing names of the attendees.')
    parser.add_argument('--custom-name', dest="custom_name", help='Custom name as prefix to every promo code', default=None)
    parser.add_argument('--domain', help='File containing names of the attendees.', choices=TDL_LIST, default='com')
    parser.add_argument('-o', '--output-file', dest="output_file", help='Directory to save the uuids generated.', default='codes.csv')
    parser.add_argument('--qr', '--save_qr', dest='qr', help='Flag to save qr for every promo code.', default=False, action='store_true')
    parser.add_argument('--id', '--event', dest='event_id',help='Event id.')
    parser.add_argument('--output-dir', dest='qr_directory',help='Directory to save the qr for every promo code.', default=None)
    args = vars(parser.parse_args())

    assert not args['qr'] or args['event_id'] is not None, 'Event id is required to save qr codes.'
    assert not args['qr'] or args['event_id'] is not None, 'Event id is required to save qr codes.'
    assert args['qr'] != args['count'], 'Cannot save qr codes and uuids in the same file.'
    assert args['count'] is None or 0 < args['count'] < 500, "Count must be between 0 and 500."
    assert os.path.exists(args['filename']) and os.path.isfile(args['filename']), 'File does not exist.'
    
    if args['qr_directory'] is not None and not os.path.exists(args['qr_directory']):
        os.makedirs(args['qr_directory'])
    if args['qr_directory'] is None:
        args['qr_directory'] = '.'

    if args['count'] is not None:
        names = map(str, range(args['count']))
    else:
        names = get_names_from_file(args['filename'])

    write_promo_code(names, **args)

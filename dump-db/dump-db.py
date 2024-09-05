import subprocess
import os

def dump_database(host, port, username, password, database, output_file):
    command = [
        'pg_dump',
        f'--host={host}',
        f'--port={port}',
        f'--username={username}',
        f'--dbname={database}',
        f'--file={output_file}',
    ]
    
    env = {'PGPASSWORD': password}
    
    try:
        subprocess.run(command, env=env, check=True)
        print(f"Database '{database}' dumped successfully to '{output_file}'.")
    except subprocess.CalledProcessError as e:
        print(f"Error dumping database: {e}")

def deploy_database(host, port, username, password, database, dump_file):
    command = [
        'psql',
        f'--host={host}',
        f'--port={port}',
        f'--username={username}',
        f'--dbname={database}',
        f'--file={dump_file}',
    ]
    
    env = {'PGPASSWORD': password}
  
    try:
        subprocess.run(command, env=env, check=True)
        print(f"Database dump '{dump_file}' deployed successfully to '{database}'.")
    except subprocess.CalledProcessError as e:
        print(f"Error deploying database dump: {e}")

def drop_database(host, port, username, password, database):
    command = [
        'dropdb',
        f'--if-exists',
        f'--host={host}',
        f'--port={port}',
        f'--username={username}',
        f'{database}',
        '-f'
    ]
    
    env = {'PGPASSWORD': password}
    
    try:
        subprocess.run(command, env=env, check=True)
        print(f"Database '{database}' dropped successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error dropping database: {e}")

def create_database(host, port, username, password, database):
    command = [
        'createdb',
        f'--host={host}',
        f'--port={port}',
        f'--username={username}',
        f'{database}',
    ]
    
    env = {'PGPASSWORD': password}
    
    try:
        subprocess.run(command, env=env, check=True)
        print(f"Database '{database}' created successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error creating database: {e}")

# directory_path = '/home/tarun/Desktop/'
# dump_file = os.path.join(directory_path, 'dump.sql')



if __name__ == "__main__":
    dump_file = 'dump.sql'

    source_database = {
        'host': 'localhost',
        'port': '9876',
        'username': 'user',
        'password': 'password',
        'database': 'postgres',
}

    target_database = {
        'host': 'localhost',
        'port': '5432',
        'username': 'user-des',
        'password': 'password-des',
        'database': 'postgres',
}
    dump_database(output_file=dump_file, **source_database) 
    drop_database(**target_database)  
    create_database(**target_database)  
    deploy_database(dump_file=dump_file, **target_database)  



import os

items_to_replace = {
    '__feature__playlist_calculator_result': '{{ duration }}'
}

for root, dirs, files in os.walk('youtube_calculator/hugo_output/public'):
    print('hello 2998', root, dirs, files, 'hello 2998')
    for file_name in files:
        if file_name == '.DS_Store':
            continue
        file_path = os.path.join(root, file_name)
        with open(file_path) as f:
            print(file_path)
            contents = f.read()
            if str(file_name).endswith('.html'):
                for before, after in items_to_replace.items():
                    contents = contents.replace(before, after)
        out_root = root.replace('hugo_output', 'hugo_output_processed')
        out_dir = os.path.join(out_root, *dirs)
        file_path_out = file_path.replace('hugo_output', 'hugo_output_processed') #= os.path.join(out_root, *dirs, file_name)
        if not os.path.exists(out_dir):
            os.makedirs(out_dir)
        with open(file_path_out, 'w') as f_out:
            f_out.write(contents)
        if file_name.endswith('.css'):
            with open('youtube_calculator/static/css/' + file_name, 'w') as f_out:
                f_out.write(contents)
        if file_name.endswith('.html'):
            with open ('youtube_calculator/templates/' + file_name, 'w') as f_out:
                f_out.write(contents)




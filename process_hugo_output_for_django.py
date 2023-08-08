import os

items_to_replace = {
    '__feature__playlist_calculator_result': '{{ duration }}'
}

css_file_names = []
for root, dirs, files in os.walk('youtube_calculator/hugo_output/public'):
    for file_name in files:
        if file_name.endswith('.css'):
            css_file_names.append(file_name)

for root, dirs, files in os.walk('youtube_calculator/hugo_output/public'):
    # print('hello 2998', root, dirs, files, 'hello 2998')
    for file_name in files:
        if file_name == '.DS_Store':
            continue
        file_path = os.path.join(root, file_name)
        with open(file_path) as f:
            # print(file_path)
            contents = f.read()
            if str(file_name).endswith('.html'):
                for before, after in items_to_replace.items():
                    contents = contents.replace(before, after)
                for css_file_name in css_file_names:
                    contents = contents.replace(
                        '/css/' + css_file_name,
                        "{{url_for('static',filename='" + css_file_name + "')}}"
                    )
        out_root = root.replace('hugo_output', 'hugo_output_processed')
        file_path = file_path.replace('hugo_output', 'hugo_output_processed')
        # file_path_out = os.path.join(out_dir, file_name)
        file_path_out = file_path.replace('hugo_output', 'hugo_output_processed') #= os.path.join(out_root, *dirs, file_name)
        if not os.path.exists(file_path[:-1]):
            os.makedirs(file_path[:-1])
        with open(file_path, 'w') as f_out:
            f_out.write(contents)
        if file_name.endswith('.css'):
            my_file_path = 'youtube_calculator/static/css/' + file_name
            print('writing css to: ' + my_file_path)
            with open(my_file_path, 'w') as f_out:
                f_out.write(contents)
        if file_name.endswith('.html'):
            out_path_now = 'youtube_calculator/templates/' + os.path.join(*file_path_out.split('/')[3:])
            out_path_dir = out_path_now[:-1]
            if not os.path.exists(out_path_dir):
                os.makedirs(out_path_dir)
            print('writing html to: ' + out_path_now)
            with open(out_path_now, 'w') as f_out:
                f_out.write(contents)




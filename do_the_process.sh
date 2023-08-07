cd hugogen
hugo
cd ..

cp -r hugogen/public/*
rm -r youtube_calculator/hugo_output/public/*
touch youtube_calculator/hugo_output/public/.exists
rm -r youtube_calculator/hugo_output_processed/public/*
touch youtube_calculator/hugo_output_processed/public/.exists
cp -r hugogen/public/* youtube_calculator/hugo_output/public/
python process_hugo_output_for_django.py
#!/usr/bin/env python3
import re
import os
import sys

def convert_urls(html_content, base_path=""):
    """Convert absolute URLs to relative paths for GitHub Pages"""
    
    # Calculate relative path depth (e.g., "../" for services/, "../../" for deeper)
    depth = base_path.count("/")
    prefix = "../" * depth if depth > 0 else ""
    
    # CSS files - convert to relative paths
    html_content = re.sub(
        r'https://cdn\.prod\.website-files\.com/64f76c0c355041d56f1b4aad/css/[^"]+\.css',
        lambda m: f'{prefix}css/webflow.shared.css',
        html_content
    )
    html_content = re.sub(
        r'//cdn\.jsdelivr\.net/npm/slick-carousel@1\.8\.1/slick/slick\.css',
        f'{prefix}css/slick.css',
        html_content
    )
    html_content = re.sub(
        r'//cdn\.jsdelivr\.net/npm/slick-carousel@1\.8\.1/slick/slick-theme\.css',
        f'{prefix}css/slick-theme.css',
        html_content
    )
    html_content = re.sub(
        r'https://cdnjs\.cloudflare\.com/ajax/libs/egjs-flicking/[^"]+\.css',
        '',
        html_content
    )
    
    # JavaScript files - convert to relative paths
    html_content = re.sub(
        r'https://d3e54v103j8qbb\.cloudfront\.net/js/jquery-3\.5\.1\.min\.[^"]+\.js[^"]*',
        f'{prefix}js/jquery.min.js',
        html_content
    )
    html_content = re.sub(
        r'https://cdn\.prod\.website-files\.com/64f76c0c355041d56f1b4aad/js/webflow\.schunk\.1a807f015b216e46\.js',
        f'{prefix}js/webflow.schunk.1.js',
        html_content
    )
    html_content = re.sub(
        r'https://cdn\.prod\.website-files\.com/64f76c0c355041d56f1b4aad/js/webflow\.schunk\.68914ce778197437\.js',
        f'{prefix}js/webflow.schunk.2.js',
        html_content
    )
    html_content = re.sub(
        r'https://cdn\.prod\.website-files\.com/64f76c0c355041d56f1b4aad/js/webflow\.abdbb8f0\.[^"]+\.js',
        f'{prefix}js/webflow.main.js',
        html_content
    )
    html_content = re.sub(
        r'//cdn\.jsdelivr\.net/npm/slick-carousel@1\.8\.1/slick/slick\.min\.js',
        f'{prefix}js/slick.min.js',
        html_content
    )
    html_content = re.sub(
        r'https://unpkg\.com/typer-dot-js@0\.1\.0/typer\.js',
        f'{prefix}js/typer.js',
        html_content
    )
    html_content = re.sub(
        r'https://ajax\.googleapis\.com/ajax/libs/webfont/1\.6\.26/webfont\.js',
        f'{prefix}js/webfont.js',
        html_content
    )
    html_content = re.sub(
        r'https://cdn\.jsdelivr\.net/gh/Flowappz/cookie-consent-cdn@v1\.1\.15/cookie-consent\.js',
        '',
        html_content
    )
    
    # Images - convert to relative paths
    html_content = re.sub(
        r'https://cdn\.prod\.website-files\.com/64f76c0c355041d56f1b4aad/64f76c0c355041d56f1b4abf_Subtract\.svg',
        f'{prefix}images/logo.svg',
        html_content
    )
    html_content = re.sub(
        r'https://cdn\.prod\.website-files\.com/64f76c0c355041d56f1b4aad/64f76c0c355041d56f1b4acf_acceltra-fav-icon32\.png',
        f'{prefix}images/favicon.png',
        html_content
    )
    html_content = re.sub(
        r'https://cdn\.prod\.website-files\.com/64f76c0c355041d56f1b4aad/6511c9044b8608e33f24933b_Screen%20Shot%202023-09-25%20at%2019\.51\.57\.png',
        f'{prefix}images/apple-touch-icon.png',
        html_content
    )
    html_content = re.sub(
        r'https://cdn\.prod\.website-files\.com/64f76c0c355041d56f1b4aad/64f76c0c355041d56f1b4ad0_companies-logo\.svg',
        f'{prefix}images/companies-logo.svg',
        html_content
    )
    html_content = re.sub(
        r'https://cdn\.prod\.website-files\.com/64f76c0c355041d56f1b4aad/64f76c0c355041d56f1b4ac3_Rectangle%2018\.webp',
        f'{prefix}images/rectangle-18.webp',
        html_content
    )
    html_content = re.sub(
        r'https://cdn\.prod\.website-files\.com/64f76c0c355041d56f1b4aad/64f76c0c355041d56f1b4abe_mobile\.webp',
        f'{prefix}images/mobile.webp',
        html_content
    )
    html_content = re.sub(
        r'https://cdn\.prod\.website-files\.com/64f76c0c355041d56f1b4aad/66be198fd89114464f7129e3_image\.png',
        f'{prefix}images/language-flag.png',
        html_content
    )
    html_content = re.sub(
        r'https://cdn\.prod\.website-files\.com/64f76c0c355041d56f1b4aad/66bf161a24e472957ad70073_Vector%20\(7\)\.png',
        f'{prefix}images/linkedin-icon.png',
        html_content
    )
    
    # Service images
    html_content = re.sub(
        r'https://cdn\.prod\.website-files\.com/650e5b3a0d853f8ef53e403a/6511ac19a4294b841afca13d_digital[^"]*\.png',
        f'{prefix}images/digital.png',
        html_content
    )
    html_content = re.sub(
        r'https://cdn\.prod\.website-files\.com/650e5b3a0d853f8ef53e403a/65115eec4df8db4740f1fde5_agile[^"]*\.png',
        f'{prefix}images/agile.png',
        html_content
    )
    html_content = re.sub(
        r'https://cdn\.prod\.website-files\.com/650e5b3a0d853f8ef53e403a/6511a9300c3a95ad59c23d48_cloud[^"]*\.png',
        f'{prefix}images/cloud.png',
        html_content
    )
    html_content = re.sub(
        r'https://cdn\.prod\.website-files\.com/650e5b3a0d853f8ef53e403a/6511aae2d7eeebdd3c9b0dd7_devops[^"]*\.png',
        f'{prefix}images/devops.png',
        html_content
    )
    html_content = re.sub(
        r'https://cdn\.prod\.website-files\.com/650e5b3a0d853f8ef53e403a/650e82e0f72127430405bf93_sre[^"]*\.webp',
        f'{prefix}images/sre.webp',
        html_content
    )
    html_content = re.sub(
        r'https://cdn\.prod\.website-files\.com/650e5b3a0d853f8ef53e403a/650e84cfd63de9da41093d25_sec[^"]*\.png',
        f'{prefix}images/sec.png',
        html_content
    )
    html_content = re.sub(
        r'https://cdn\.prod\.website-files\.com/650e5b3a0d853f8ef53e403a/650e843238fe3eaebe22eace_software[^"]*\.jpeg',
        f'{prefix}images/software.jpeg',
        html_content
    )
    html_content = re.sub(
        r'https://cdn\.prod\.website-files\.com/650e5b3a0d853f8ef53e403a/6511bc2ae7169a6dcf82b05b_data2[^"]*\.png',
        f'{prefix}images/data2.png',
        html_content
    )
    html_content = re.sub(
        r'https://cdn\.prod\.website-files\.com/650e5b3a0d853f8ef53e403a/6511ba57e8eec1e208f3567a_ai2[^"]*\.png',
        f'{prefix}images/ai2.png',
        html_content
    )
    html_content = re.sub(
        r'https://cdn\.prod\.website-files\.com/650e5b3a0d853f8ef53e403a/6511bd738b55feccf59ca53b_tech1[^"]*\.png',
        f'{prefix}images/tech1.png',
        html_content
    )
    
    # Hero background image
    html_content = re.sub(
        r'https://cdn\.prod\.website-files\.com/64f76c0c355041d56f1b4aad/650e385f25167461fbbdd0cc_[^"]*\.png',
        f'{prefix}images/hero-bg.png',
        html_content
    )
    html_content = re.sub(
        r'https://cdn\.prod\.website-files\.com/64f76c0c355041d56f1b4aad/6511cf4b7f1d03a7828e6604_world\.jpg',
        f'{prefix}images/world.jpg',
        html_content
    )
    
    # Fix internal links - convert absolute paths to relative
    # Root links
    html_content = re.sub(
        r'href="/"',
        f'href="{prefix}index.html"',
        html_content
    )
    html_content = re.sub(
        r'href="/#services"',
        f'href="{prefix}index.html#services"',
        html_content
    )
    html_content = re.sub(
        r'href="/#contact"',
        f'href="{prefix}index.html#contact"',
        html_content
    )
    
    # Legal pages
    html_content = re.sub(
        r'href="/impressum"',
        f'href="{prefix}impressum.html"',
        html_content
    )
    html_content = re.sub(
        r'href="/tos"',
        f'href="{prefix}tos.html"',
        html_content
    )
    html_content = re.sub(
        r'href="/privacy"',
        f'href="{prefix}privacy.html"',
        html_content
    )
    
    # Service pages - convert to relative paths
    service_pages = [
        'digital-strategy', 'agile-transformation', 'cloud', 'devops-consulting',
        'sre-consulting', 'cyber-security', 'software-development', 'data-science',
        'artificial-intelligence', 'technology-solutions'
    ]
    for service in service_pages:
        html_content = re.sub(
            rf'href="/services/{service}"',
            f'href="{prefix}services/{service}.html"',
            html_content
        )
    
    # Solution pages
    solution_pages = ['bestmodal', 'cargoflo', 'storylob']
    for solution in solution_pages:
        html_content = re.sub(
            rf'href="/solutions/{solution}"',
            f'href="{prefix}solutions/{solution}.html"',
            html_content
        )
    
    # Remove integrity and crossorigin attributes from converted links
    html_content = re.sub(
        r'\s+integrity="[^"]*"',
        '',
        html_content
    )
    html_content = re.sub(
        r'\s+crossorigin="[^"]*"',
        '',
        html_content
    )
    
    # Remove empty link tags
    html_content = re.sub(
        r'<link rel="stylesheet" href=""\s*/>',
        '',
        html_content
    )
    html_content = re.sub(
        r'<script src=""></script>',
        '',
        html_content
    )
    
    # Remove Webflow badge
    html_content = re.sub(
        r'<a class="w-webflow-badge"[^>]*>.*?</a>',
        '',
        html_content,
        flags=re.DOTALL
    )
    
    return html_content

# Process service pages
service_files = [
    'digital-strategy_raw.html', 'agile-transformation_raw.html', 'cloud_raw.html',
    'devops-consulting_raw.html', 'sre-consulting_raw.html', 'cyber-security_raw.html',
    'software-development_raw.html', 'data-science_raw.html', 'artificial-intelligence_raw.html',
    'technology-solutions_raw.html'
]

for input_file in service_files:
    input_path = f'services/{input_file}'
    output_file = input_file.replace('_raw.html', '.html')
    output_path = f'services/{output_file}'
    
    if os.path.exists(input_path):
        with open(input_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        converted = convert_urls(content, 'services/')
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(converted)
        
        print(f'Converted {input_path} -> {output_path}')

# Process solution pages
solution_files = ['bestmodal_raw.html', 'cargoflo_raw.html', 'storylob_raw.html']

for input_file in solution_files:
    input_path = f'solutions/{input_file}'
    output_file = input_file.replace('_raw.html', '.html')
    output_path = f'solutions/{output_file}'
    
    if os.path.exists(input_path):
        with open(input_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        converted = convert_urls(content, 'solutions/')
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(converted)
        
        print(f'Converted {input_path} -> {output_path}')

print('All files converted!')

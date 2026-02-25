"""
Run this once after migrations to populate your blog with the original posts:
    python seed.py
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from blog.models import Post, PostContent

# Clear existing data
Post.objects.all().delete()

# ── Post 1: Spider-Man ────────────────────────────────────────────────────────
p1 = Post.objects.create(
    title='Analysis of science-fiction shows in the 1990s',
    slug='spider-man',
    author='Nicolas Garlinski',
    nav_label='Spider-Man',
    is_new=True,
    hero_image='https://res.cloudinary.com/dfog0e294/image/upload/v1547130131/webdev/Blog/spider-post-01.png',
    hero_image_alt='Space Stations and Style: A Look at the Designs of Babylon 5 and DS9',
)
PostContent.objects.create(post=p1, type='lead', order=1, text=(
    'Babylon 5 and Star Trek: Deep Space Nine (DS9) have distinct approaches to set and character design, '
    'reflecting their differing tones and settings. Babylon 5 is known for its more industrial and utilitarian '
    'aesthetic. The space station itself is a massive, angular structure that emphasizes a gritty, lived-in feel, '
    'with darker lighting and minimalistic sets. In contrast, DS9 features a more polished, brighter design, '
    'with its space station having a more expansive, intricate, and somewhat alien look due to its Bajoran origins.'
))
PostContent.objects.create(post=p1, type='text', order=2, text=(
    'Vestibulum vehicula quam id quam lobortis convallis. Nullam quis pulvinar dolor. Pellentesque semper '
    'bibendum facilisis. Ut vitae interdum tortor. Etiam mattis dui ut dui pharetra, ac auctor ligula rhoncus.'
))
PostContent.objects.create(
    post=p1, type='image', order=3,
    image_url='https://res.cloudinary.com/dfog0e294/image/upload/v1547130606/webdev/Blog/spider-post-02.png',
    image_alt='Lego Spider-Man',
)
PostContent.objects.create(
    post=p1, type='blockquote', order=4,
    text='Nam nec lectus in nulla interdum ultrices mollis id dui. Duis sed sapien eu felis elementum scelerisque.',
    blockquote_footer='Someone in Gotham',
)
PostContent.objects.create(
    post=p1, type='image', order=5,
    image_url='https://res.cloudinary.com/dfog0e294/image/upload/v1547130607/webdev/Blog/spider-post-03.png',
    image_alt='Lego Spider-Man',
)
PostContent.objects.create(post=p1, type='text', order=6, text=(
    'In hac habitasse platea dictumst. Curabitur vulputate, nunc sed tempus vehicula, turpis urna mattis augue, '
    'sed lobortis urna magna id libero. Nam eget erat mattis, molestie lorem id, pharetra nisl.'
))

# ── Post 2: Batman ────────────────────────────────────────────────────────────
p2 = Post.objects.create(
    title='Batman Adventures',
    slug='batman',
    author='Nicolas Garlinski',
    nav_label='Batman',
    is_new=False,
    hero_image='https://res.cloudinary.com/dfog0e294/image/upload/v1547130130/webdev/Blog/batman-post-01.jpg',
    hero_image_alt='Lego Batman',
)
PostContent.objects.create(post=p2, type='lead', order=1, text=(
    'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer facilisis sollicitudin nisl non dignissim. '
    'Phasellus hendrerit nisl et massa cursus suscipit. Donec pulvinar diam dolor, sit amet vestibulum purus.'
))
PostContent.objects.create(post=p2, type='text', order=2, text=(
    'Vestibulum vehicula quam id quam lobortis convallis. Nullam quis pulvinar dolor. Pellentesque semper '
    'bibendum facilisis. Ut vitae interdum tortor.'
))
PostContent.objects.create(
    post=p2, type='blockquote', order=3,
    text='Nam nec lectus in nulla interdum ultrices mollis id dui. Pellentesque vehicula sed turpis eget pellentesque.',
    blockquote_footer='Someone in Gotham',
)
PostContent.objects.create(
    post=p2, type='image', order=4,
    image_url='https://res.cloudinary.com/dfog0e294/image/upload/v1547468714/webdev/Blog/batman-post-02.jpg',
    image_alt='Lego Batman',
)
PostContent.objects.create(post=p2, type='text', order=5, text=(
    'In hac habitasse platea dictumst. Curabitur vulputate, nunc sed tempus vehicula, turpis urna mattis augue.'
))

# ── Post 3: Panther ───────────────────────────────────────────────────────────
p3 = Post.objects.create(
    title='Black Panther Adventures',
    slug='panther',
    author='Nicolas Garlinski',
    nav_label='Panther',
    is_new=False,
    hero_image='https://res.cloudinary.com/dfog0e294/image/upload/v1547131038/webdev/Blog/panther-post-01.png',
    hero_image_alt='Lego Panther',
)
PostContent.objects.create(post=p3, type='lead', order=1, text=(
    'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer facilisis sollicitudin nisl non dignissim.'
))
PostContent.objects.create(post=p3, type='text', order=2, text=(
    'Vestibulum vehicula quam id quam lobortis convallis. Nullam quis pulvinar dolor.'
))
PostContent.objects.create(
    post=p3, type='image', order=3,
    image_url='https://res.cloudinary.com/dfog0e294/image/upload/v1547469074/webdev/Blog/panther-post-02.jpg',
    image_alt='Lego Panther',
)
PostContent.objects.create(
    post=p3, type='blockquote', order=4,
    text='Nam nec lectus in nulla interdum ultrices mollis id dui. Vivamus pharetra odio quis placerat pulvinar.',
    blockquote_footer='Someone in Gotham',
)
PostContent.objects.create(post=p3, type='text', order=5, text=(
    'In hac habitasse platea dictumst. Curabitur vulputate, nunc sed tempus vehicula.'
))

print('✅ Database seeded with 3 blog posts!')

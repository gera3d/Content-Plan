import rss from '@astrojs/rss';
import { getCollection } from 'astro:content';
import type { APIContext } from 'astro';

export async function GET(context: APIContext) {
    const posts = await getCollection('posts', ({ data }) => !data.draft);

    // Sort by date, newest first
    const sortedPosts = posts.sort((a, b) =>
        b.data.publishDate.valueOf() - a.data.publishDate.valueOf()
    );

    return rss({
        title: 'Gera Yeremin',
        description: 'I build custom software for businesses that have outgrown spreadsheets. Developer + Marketer.',
        site: context.site || 'https://gera.yere.in',
        items: sortedPosts.map((post) => ({
            title: post.data.title,
            description: post.data.description,
            pubDate: post.data.publishDate,
            link: `/${post.slug}/`,
            author: post.data.author,
            categories: [post.data.topic, ...post.data.tags],
        })),
        customData: `<language>en-us</language>`,
    });
}

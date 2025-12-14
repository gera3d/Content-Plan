import { z, defineCollection } from 'astro:content';

const posts = defineCollection({
    type: 'content',
    schema: z.object({
        title: z.string(),
        description: z.string(),
        publishDate: z.coerce.date(),
        updatedDate: z.coerce.date().optional(),
        author: z.string().default('Gera Yeremin'),
        topic: z.enum(['software-development', 'digital-marketing', 'business-automation']),
        tags: z.array(z.string()).default([]),
        featured: z.boolean().default(false),
        draft: z.boolean().default(false),
    }),
});

export const collections = { posts };

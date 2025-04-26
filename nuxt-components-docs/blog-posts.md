<!-- source: https://ui.nuxt.com/components/blog-posts --> # BlogPostsPRO

[GitHub](https://github.com/nuxt/ui-
pro/tree/v3/src/runtime/components/BlogPosts.vue)

Display a list of blog posts in a responsive grid layout.

## Usage

The BlogPosts component provides a flexible layout to display a list of
[BlogPost](/components/blog-post) components using either the default slot or
the `posts` prop.

    
    
    <template>
      <UBlogPosts>
        <UBlogPost
          v-for="(post, index) in posts"
          :key="index"
          v-bind="post"
        />
      </UBlogPosts>
    </template>
    

### Posts

Use the `posts` prop as an array of objects with the properties of the
[BlogPost](/components/blog-post#props) component.

![Nuxt Icon v1](https://nuxt.com/assets/blog/nuxt-icon/cover.png)

Nov 25, 2024

## Nuxt Icon v1

Discover Nuxt Icon v1!

![Nuxt 3.14](https://nuxt.com/assets/blog/v3.14.png)

Nov 4, 2024

## Nuxt 3.14

Nuxt 3.14 is out!

![Nuxt 3.13](https://nuxt.com/assets/blog/v3.13.png)

Aug 22, 2024

## Nuxt 3.13

Nuxt 3.13 is out!

    
    
    <script setup lang="ts">
    const posts = ref([
      {
        title: 'Nuxt Icon v1',
        description: 'Discover Nuxt Icon v1!',
        image: 'https://nuxt.com/assets/blog/nuxt-icon/cover.png',
        date: '2024-11-25'
      },
      {
        title: 'Nuxt 3.14',
        description: 'Nuxt 3.14 is out!',
        image: 'https://nuxt.com/assets/blog/v3.14.png',
        date: '2024-11-04'
      },
      {
        title: 'Nuxt 3.13',
        description: 'Nuxt 3.13 is out!',
        image: 'https://nuxt.com/assets/blog/v3.13.png',
        date: '2024-08-22'
      }
    ])
    </script>
    
    <template>
      <UBlogPosts :posts="posts" />
    </template>
    

Expand code

### Orientation

Use the `orientation` prop to change the orientation of the BlogPosts.
Defaults to `horizontal`.

orientation

vertical

![Nuxt Icon v1](https://nuxt.com/assets/blog/nuxt-icon/cover.png)

Nov 25, 2024

## Nuxt Icon v1

Discover Nuxt Icon v1!

![Nuxt 3.14](https://nuxt.com/assets/blog/v3.14.png)

Nov 4, 2024

## Nuxt 3.14

Nuxt 3.14 is out!

![Nuxt 3.13](https://nuxt.com/assets/blog/v3.13.png)

Aug 22, 2024

## Nuxt 3.13

Nuxt 3.13 is out!

    
    
    <script setup lang="ts">
    const posts = ref([
      {
        title: 'Nuxt Icon v1',
        description: 'Discover Nuxt Icon v1!',
        image: 'https://nuxt.com/assets/blog/nuxt-icon/cover.png',
        date: '2024-11-25'
      },
      {
        title: 'Nuxt 3.14',
        description: 'Nuxt 3.14 is out!',
        image: 'https://nuxt.com/assets/blog/v3.14.png',
        date: '2024-11-04'
      },
      {
        title: 'Nuxt 3.13',
        description: 'Nuxt 3.13 is out!',
        image: 'https://nuxt.com/assets/blog/v3.13.png',
        date: '2024-08-22'
      }
    ])
    </script>
    
    <template>
      <UBlogPosts orientation="vertical" :posts="posts" />
    </template>
    

Expand code

When using the `posts` prop instead of the default slot, the `orientation` of
the posts is automatically reversed, `horizontal` to `vertical` and vice
versa.

## Examples

While these examples use [Nuxt Content](https://content.nuxt.com), the
components can be integrated with any content management system.

### Within a page

Use the BlogPosts component in a page to create a blog page:

pages/blog/index.vue

    
    
    <script setup lang="ts">
    const { data: posts } = await useAsyncData('posts', () => queryCollection('posts').all())
    </script>
    
    <template>
      <UPage>
        <UPageHero title="Blog" />
    
        <UPageBody>
          <UContainer>
            <UBlogPosts>
              <UBlogPost
                v-for="(post, index) in posts"
                :key="index"
                v-bind="post"
                :to="post.path"
              />
            </UBlogPosts>
          </UContainer>
        </UPageBody>
      </UPage>
    </template>
    

In this example, the `posts` are fetched using `queryCollection` from the
`@nuxt/content` module.

The `to` prop is overridden here since `@nuxt/content` uses the `path`
property.

## API

### Props

Prop |  Default |  Type   
---|---|---  
`as`| `'div'`| `any`The element or component this component should render as.  
`orientation`| `'horizontal'`| ` "horizontal" | "vertical"`  
`posts`| | ` BlogPostProps[]`Show properties

  * `as?: any`The element or component this component should render as. Defaults to `'article'`.
  * `title?: string`
  * `description?: string`
  * `date?: string | Date`The date of the blog post. Can be a string or a Date object.
  * `badge?: string | BadgeProps`Display a badge on the blog post. Can be a string or an object. `{ color: 'neutral', variant: 'subtle' }`
  * `authors?: UserProps[]`The authors of the blog post.
  * `image?: string | Partial<HTMLImageElement>`The image of the blog post. Can be a string or an object.
  * `orientation?: "horizontal" | "vertical"`The orientation of the blog post. Defaults to `'vertical'`.
  * `variant?: "outline" | "soft" | "subtle" | "ghost" | "naked"`Defaults to `'outline'`.
  * `to?: string | RouteLocationAsRelativeGeneric | RouteLocationAsPathGeneric`
  * `target?: "_blank" | "_parent" | "_self" | "_top" | (string & {}) | null`
  * `class?: any`
  * `ui?: { root?: ClassNameValue; header?: ClassNameValue; body?: ClassNameValue; footer?: ClassNameValue; image?: ClassNameValue; ... 6 more ...; badge?: ClassNameValue; }`

  
  
### Slots

Slot |  Type   
---|---  
`default`| `{}`  
  
## Theme

app.config.ts

    
    
    export default defineAppConfig({
      uiPro: {
        blogPosts: {
          base: 'flex flex-col gap-8 lg:gap-y-16',
          variants: {
            orientation: {
              horizontal: 'sm:grid sm:grid-cols-2 lg:grid-cols-3',
              vertical: ''
            }
          }
        }
      }
    })
    

Expand code

vite.config.ts

    
    
    import { defineConfig } from 'vite'
    import vue from '@vitejs/plugin-vue'
    import ui from '@nuxt/ui/vite'
    
    export default defineConfig({
      plugins: [
        vue(),
        ui({
          uiPro: {
            blogPosts: {
              base: 'flex flex-col gap-8 lg:gap-y-16',
              variants: {
                orientation: {
                  horizontal: 'sm:grid sm:grid-cols-2 lg:grid-cols-3',
                  vertical: ''
                }
              }
            }
          }
        })
      ]
    })
    

Expand code

vite.config.ts

    
    
    import { defineConfig } from 'vite'
    import vue from '@vitejs/plugin-vue'
    import uiPro from '@nuxt/ui-pro/vite'
    
    export default defineConfig({
      plugins: [
        vue(),
        uiPro({
          uiPro: {
            blogPosts: {
              base: 'flex flex-col gap-8 lg:gap-y-16',
              variants: {
                orientation: {
                  horizontal: 'sm:grid sm:grid-cols-2 lg:grid-cols-3',
                  vertical: ''
                }
              }
            }
          }
        })
      ]
    })
    

Expand code

[BlogPostA customizable article to display in a blog page.](/components/blog-
post)[BreadcrumbA hierarchy of links to navigate through a
website.](/components/breadcrumb)


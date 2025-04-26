<!-- source: https://ui.nuxt.com/components/blog-post --> # BlogPostPRO

[GitHub](https://github.com/nuxt/ui-
pro/tree/v3/src/runtime/components/BlogPost.vue)

A customizable article to display in a blog page.

## Usage

The BlogPost component provides a flexible way to display an `<article>`
element with customizable content including title, description, image, etc.

![Introducing Nuxt Icon v1](https://nuxt.com/assets/blog/nuxt-icon/cover.png)

[](https://nuxt.com/blog/nuxt-icon-v1-0)

Nov 25, 2024

## Introducing Nuxt Icon v1

Discover Nuxt Icon v1 - a modern, versatile, and customizable icon solution
for your Nuxt projects.

![Anthony Fu](https://github.com/antfu.png)

[](https://github.com/antfu)

Anthony Fu

antfu7

[](/components/blog-posts)Use the [`BlogPosts`](/components/blog-posts)
component to display multiple blog posts in a responsive grid layout.

### Title

Use the `title` prop to display the title of the BlogPost.

title

## Introducing Nuxt Icon v1

    
    
    <template>
      <UBlogPost title="Introducing Nuxt Icon v1" />
    </template>
    

### Description

Use the `description` prop to display the description of the BlogPost.

description

## Introducing Nuxt Icon v1

Discover Nuxt Icon v1 - a modern, versatile, and customizable icon solution
for your Nuxt projects.

    
    
    <template>
      <UBlogPost
        title="Introducing Nuxt Icon v1"
        description="Discover Nuxt Icon v1 - a modern, versatile, and customizable icon solution for your Nuxt projects."
      />
    </template>
    

### Date

Use the `date` prop to display the date of the BlogPost.

The date is automatically formatted to the [current locale](/getting-
started/i18n/nuxt#locale). You can either pass a `Date` object or a string.

date

Nov 25, 2024

## Introducing Nuxt Icon v1

Discover Nuxt Icon v1 - a modern, versatile, and customizable icon solution
for your Nuxt projects.

    
    
    <template>
      <UBlogPost
        title="Introducing Nuxt Icon v1"
        description="Discover Nuxt Icon v1 - a modern, versatile, and customizable icon solution for your Nuxt projects."
        date="2024-11-25"
      />
    </template>
    

### Badge

Use the `badge` prop to display a [Badge](/components/badge) in the BlogPost.

badge

Release

## Introducing Nuxt Icon v1

Discover Nuxt Icon v1 - a modern, versatile, and customizable icon solution
for your Nuxt projects.

    
    
    <template>
      <UBlogPost
        title="Introducing Nuxt Icon v1"
        description="Discover Nuxt Icon v1 - a modern, versatile, and customizable icon solution for your Nuxt projects."
        badge="Release"
      />
    </template>
    

You can pass any property from the [Badge](/components/badge#props) component
to customize it.

Release

## Introducing Nuxt Icon v1

Discover Nuxt Icon v1 - a modern, versatile, and customizable icon solution
for your Nuxt projects.

    
    
    <template>
      <UBlogPost
        title="Introducing Nuxt Icon v1"
        description="Discover Nuxt Icon v1 - a modern, versatile, and customizable icon solution for your Nuxt projects."
        :badge="{
          label: 'Release',
          color: 'primary',
          variant: 'solid'
        }"
      />
    </template>
    

### Image

Use the `image` prop to display an image in the BlogPost.

If [`@nuxt/image`](https://image.nuxt.com/get-started/installation) is
installed, the `<NuxtImg>` component will be used instead of the native `img`
tag.

image

![Introducing Nuxt Icon v1](https://nuxt.com/assets/blog/nuxt-icon/cover.png)

Nov 25, 2024

## Introducing Nuxt Icon v1

Discover Nuxt Icon v1 - a modern, versatile, and customizable icon solution
for your Nuxt projects.

    
    
    <template>
      <UBlogPost
        title="Introducing Nuxt Icon v1"
        description="Discover Nuxt Icon v1 - a modern, versatile, and customizable icon solution for your Nuxt projects."
        image="https://nuxt.com/assets/blog/nuxt-icon/cover.png"
        date="2024-11-25"
      />
    </template>
    

### Authors

Use the `authors` prop to display a list of [User](/components/user) in the
BlogPost as an array of objects with the following properties:

  * `name?: string`
  * `description?: string`
  * `avatar?: Omit<AvatarProps, 'size'>`
  * `chip?: boolean | Omit<ChipProps, 'size' | 'inset'>`
  * `size?: UserProps['size']`
  * `orientation?: UserProps['orientation']`

You can pass any property from the [Link](/components/link#props) component
such as `to`, `target`, etc.

![Introducing Nuxt Icon v1](https://nuxt.com/assets/blog/nuxt-icon/cover.png)

Nov 25, 2024

## Introducing Nuxt Icon v1

Discover Nuxt Icon v1 - a modern, versatile, and customizable icon solution
for your Nuxt projects.

![Anthony Fu](https://github.com/antfu.png)

[](https://github.com/antfu)

Anthony Fu

antfu7

    
    
    <script setup lang="ts">
    const authors = ref([
      {
        name: 'Anthony Fu',
        description: 'antfu7',
        avatar: {
          src: 'https://github.com/antfu.png'
        },
        to: 'https://github.com/antfu',
        target: '_blank'
      }
    ])
    </script>
    
    <template>
      <UBlogPost
        title="Introducing Nuxt Icon v1"
        description="Discover Nuxt Icon v1 - a modern, versatile, and customizable icon solution for your Nuxt projects."
        image="https://nuxt.com/assets/blog/nuxt-icon/cover.png"
        date="2024-11-25"
        :authors="authors"
      />
    </template>
    

When the `authors` prop has more than one item, the
[AvatarGroup](/components/avatar-group) component is used.

![Introducing Nuxt Icon v1](https://nuxt.com/assets/blog/nuxt-icon/cover.png)

Nov 25, 2024

## Introducing Nuxt Icon v1

Discover Nuxt Icon v1 - a modern, versatile, and customizable icon solution
for your Nuxt projects.

[![](https://github.com/benjamincanac.png)](https://github.com/benjamincanac)[![](https://github.com/antfu.png)](https://github.com/antfu)

    
    
    <script setup lang="ts">
    const authors = ref([
      {
        name: 'Anthony Fu',
        description: 'antfu7',
        avatar: {
          src: 'https://github.com/antfu.png'
        },
        to: 'https://github.com/antfu',
        target: '_blank'
      },
      {
        name: 'Benjamin Canac',
        description: 'benjamincanac',
        avatar: {
          src: 'https://github.com/benjamincanac.png'
        },
        to: 'https://github.com/benjamincanac',
        target: '_blank'
      }
    ])
    </script>
    
    <template>
      <UBlogPost
        title="Introducing Nuxt Icon v1"
        description="Discover Nuxt Icon v1 - a modern, versatile, and customizable icon solution for your Nuxt projects."
        image="https://nuxt.com/assets/blog/nuxt-icon/cover.png"
        date="2024-11-25"
        :authors="authors"
      />
    </template>
    

### Link

You can pass any property from the
[`<NuxtLink>`](https://nuxt.com/docs/api/components/nuxt-link) component such
as `to`, `target`, `rel`, etc.

to

target

![Introducing Nuxt Icon v1](https://nuxt.com/assets/blog/nuxt-icon/cover.png)

[](https://nuxt.com/blog/nuxt-icon-v1-0)

Nov 25, 2024

## Introducing Nuxt Icon v1

Discover Nuxt Icon v1 - a modern, versatile, and customizable icon solution
for your Nuxt projects.

    
    
    <template>
      <UBlogPost
        title="Introducing Nuxt Icon v1"
        description="Discover Nuxt Icon v1 - a modern, versatile, and customizable icon solution for your Nuxt projects."
        image="https://nuxt.com/assets/blog/nuxt-icon/cover.png"
        date="2024-11-25"
        to="https://nuxt.com/blog/nuxt-icon-v1-0"
        target="_blank"
      />
    </template>
    

### Variant

Use the `variant` prop to change the style of the BlogPost.

variant

naked

![Introducing Nuxt Icon v1](https://nuxt.com/assets/blog/nuxt-icon/cover.png)

[](https://nuxt.com/blog/nuxt-icon-v1-0)

Nov 25, 2024

## Introducing Nuxt Icon v1

Discover Nuxt Icon v1 - a modern, versatile, and customizable icon solution
for your Nuxt projects.

    
    
    <template>
      <UBlogPost
        title="Introducing Nuxt Icon v1"
        description="Discover Nuxt Icon v1 - a modern, versatile, and customizable icon solution for your Nuxt projects."
        image="https://nuxt.com/assets/blog/nuxt-icon/cover.png"
        date="2024-11-25"
        to="https://nuxt.com/blog/nuxt-icon-v1-0"
        target="_blank"
        variant="naked"
      />
    </template>
    

The styling will be different wether you provide a `to` prop or an `image`.

### Orientation

Use the `orientation` prop to change the BlogPost orientation. Defaults to
`vertical`.

orientation

horizontal

variant

outline

![Introducing Nuxt Icon v1](https://nuxt.com/assets/blog/nuxt-icon/cover.png)

[](https://nuxt.com/blog/nuxt-icon-v1-0)

Nov 25, 2024

## Introducing Nuxt Icon v1

Discover Nuxt Icon v1 - a modern, versatile, and customizable icon solution
for your Nuxt projects.

    
    
    <template>
      <UBlogPost
        title="Introducing Nuxt Icon v1"
        description="Discover Nuxt Icon v1 - a modern, versatile, and customizable icon solution for your Nuxt projects."
        image="https://nuxt.com/assets/blog/nuxt-icon/cover.png"
        date="2024-11-25"
        to="https://nuxt.com/blog/nuxt-icon-v1-0"
        target="_blank"
        orientation="horizontal"
        variant="outline"
      />
    </template>
    

## API

### Props

Prop |  Default |  Type   
---|---|---  
`as`| `'article'`| `any`  
`orientation`| `'vertical'`| ` "horizontal" | "vertical"`  
`target`| | ` null | "_blank" | "_parent" | "_self" | "_top" | string & {}`  
`to`| | ` string | RouteLocationAsRelativeGeneric | RouteLocationAsPathGeneric`Show properties

  * `name?: RouteRecordNameGeneric`
  * `params?: RouteParamsRawGeneric`
  * `path?: undefined`A relative path to the current location. This property should be removed
  * `query?: LocationQueryRaw`
  * `hash?: string`
  * `force?: boolean`Triggers the navigation even if the location is the same as the current one. Note this will also add a new entry to the history unless `replace: true` is passed.
  * `state?: HistoryState`State to save using the History API. This cannot contain any reactive values and some primitives like Symbols are forbidden. More info at <https://developer.mozilla.org/en-US/docs/Web/API/History/state>
  * `path: string`A relative path to the current location. This property should be removed
  * `query?: LocationQueryRaw`
  * `hash?: string`
  * `force?: boolean`Triggers the navigation even if the location is the same as the current one. Note this will also add a new entry to the history unless `replace: true` is passed.
  * `state?: HistoryState`State to save using the History API. This cannot contain any reactive values and some primitives like Symbols are forbidden. More info at <https://developer.mozilla.org/en-US/docs/Web/API/History/state>

  
`title`| | ` string`  
`description`| | ` string`  
`variant`| `'outline'`| ` "outline" | "soft" | "subtle" | "ghost" | "naked"`  
`badge`| | ` string | BadgeProps`Display a badge on the blog post. Can be a string or an object. `{ color: 'neutral', variant: 'subtle' }`Show properties

  * `as?: any`The element or component this component should render as. Defaults to `'span'`.
  * `label?: string | number`
  * `color?: "error" | "primary" | "secondary" | "success" | "info" | "warning" | "neutral"`Defaults to `'primary'`.
  * `variant?: "solid" | "outline" | "soft" | "subtle"`Defaults to `'solid'`.
  * `size?: "md" | "xs" | "sm" | "lg" | "xl"`Defaults to `'md'`.
  * `class?: any`
  * `ui?: { base?: ClassNameValue; label?: ClassNameValue; leadingIcon?: ClassNameValue; leadingAvatar?: ClassNameValue; leadingAvatarSize?: ClassNameValue; trailingIcon?: ClassNameValue; }`
  * `icon?: string`Display an icon based on the `leading` and `trailing` props.
  * `trailingIcon?: string`Display an icon on the right side.
  * `leading?: boolean`When `true`, the icon will be displayed on the left side.
  * `leadingIcon?: string`Display an icon on the left side.
  * `avatar?: AvatarProps`Display an avatar on the left side.
  * `trailing?: boolean`When `true`, the icon will be displayed on the right side.

  
`image`| | ` string | Partial<HTMLImageElement>`The image of the blog post. Can be a string or an object.  
`date`| | ` string | Date`The date of the blog post. Can be a string or a Date object.  
`authors`| | ` UserProps[]`The authors of the blog post.Show properties

  * `as?: any`The element or component this component should render as. Defaults to `'div'`.
  * `name?: string`
  * `description?: string`
  * `avatar?: (Omit<AvatarProps, "size"> & { [key: string]: any; })`
  * `chip?: boolean | Omit<ChipProps, "size" | "inset">`
  * `size?: "md" | "xs" | "sm" | "lg" | "xl" | "3xs" | "2xs" | "2xl" | "3xl"`Defaults to `'md'`.
  * `orientation?: "horizontal" | "vertical"`The orientation of the user. Defaults to `'horizontal'`.
  * `to?: string | RouteLocationAsRelativeGeneric | RouteLocationAsPathGeneric`
  * `target?: "_blank" | "_parent" | "_self" | "_top" | (string & {}) | null`
  * `class?: any`
  * `ui?: { root?: ClassNameValue; wrapper?: ClassNameValue; name?: ClassNameValue; description?: ClassNameValue; avatar?: ClassNameValue; }`

  
`ui`| | ` { root?: ClassNameValue; header?: ClassNameValue; body?: ClassNameValue; footer?: ClassNameValue; image?: ClassNameValue; ... 6 more ...; badge?: ClassNameValue; }`  
  
### Slots

Slot |  Type   
---|---  
`date`| `{}`  
`badge`| `{}`  
`title`| `{}`  
`description`| `{}`  
`authors`| `{}`  
`header`| `{}`  
`body`| `{}`  
`footer`| `{}`  
  
## Theme

app.config.ts

    
    
    export default defineAppConfig({
      uiPro: {
        blogPost: {
          slots: {
            root: 'relative group/blog-post flex flex-col rounded-lg overflow-hidden',
            header: 'relative overflow-hidden aspect-[16/9] w-full pointer-events-none',
            body: 'min-w-0 flex-1 flex flex-col',
            footer: '',
            image: 'object-cover object-top w-full h-full',
            title: 'text-xl text-pretty font-semibold text-highlighted',
            description: 'mt-1 text-base text-pretty',
            authors: 'pt-4 mt-auto flex flex-wrap gap-x-3 gap-y-1.5',
            avatar: '',
            meta: 'flex items-center gap-2 mb-2',
            date: 'text-sm',
            badge: ''
          },
          variants: {
            orientation: {
              horizontal: {
                root: 'lg:grid lg:grid-cols-2 lg:items-center gap-x-8',
                body: 'justify-center p-4 sm:p-6 lg:px-0'
              },
              vertical: {
                root: 'flex flex-col',
                body: 'p-4 sm:p-6'
              }
            },
            variant: {
              outline: {
                root: 'bg-default ring ring-default',
                date: 'text-toned',
                description: 'text-muted'
              },
              soft: {
                root: 'bg-elevated/50',
                date: 'text-muted',
                description: 'text-toned'
              },
              subtle: {
                root: 'bg-elevated/50 ring ring-default',
                date: 'text-muted',
                description: 'text-toned'
              },
              ghost: {
                date: 'text-toned',
                description: 'text-muted',
                header: 'shadow-lg rounded-lg'
              },
              naked: {
                root: 'p-0 sm:p-0',
                date: 'text-toned',
                description: 'text-muted',
                header: 'shadow-lg rounded-lg'
              }
            },
            to: {
              true: {
                root: [
                  'transition'
                ],
                image: 'transform transition-transform duration-200 group-hover/blog-post:scale-110',
                avatar: 'transform transition-transform duration-200 hover:scale-115'
              }
            },
            image: {
              true: ''
            }
          },
          compoundVariants: [
            {
              variant: 'outline',
              to: true,
              class: {
                root: 'hover:bg-elevated/50'
              }
            },
            {
              variant: 'soft',
              to: true,
              class: {
                root: 'hover:bg-elevated'
              }
            },
            {
              variant: 'subtle',
              to: true,
              class: {
                root: 'hover:bg-elevated hover:ring-accented'
              }
            },
            {
              variant: 'ghost',
              to: true,
              class: {
                root: 'hover:bg-elevated/50',
                header: [
                  'group-hover/blog-post:shadow-none',
                  'transition-all'
                ]
              }
            },
            {
              variant: 'ghost',
              to: true,
              orientation: 'vertical',
              class: {
                header: 'group-hover/blog-post:rounded-b-none'
              }
            },
            {
              variant: 'ghost',
              to: true,
              orientation: 'horizontal',
              class: {
                header: 'group-hover/blog-post:rounded-r-none'
              }
            },
            {
              orientation: 'vertical',
              image: false,
              variant: 'naked',
              class: {
                body: 'p-0 sm:p-0'
              }
            }
          ],
          defaultVariants: {
            variant: 'outline'
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
            blogPost: {
              slots: {
                root: 'relative group/blog-post flex flex-col rounded-lg overflow-hidden',
                header: 'relative overflow-hidden aspect-[16/9] w-full pointer-events-none',
                body: 'min-w-0 flex-1 flex flex-col',
                footer: '',
                image: 'object-cover object-top w-full h-full',
                title: 'text-xl text-pretty font-semibold text-highlighted',
                description: 'mt-1 text-base text-pretty',
                authors: 'pt-4 mt-auto flex flex-wrap gap-x-3 gap-y-1.5',
                avatar: '',
                meta: 'flex items-center gap-2 mb-2',
                date: 'text-sm',
                badge: ''
              },
              variants: {
                orientation: {
                  horizontal: {
                    root: 'lg:grid lg:grid-cols-2 lg:items-center gap-x-8',
                    body: 'justify-center p-4 sm:p-6 lg:px-0'
                  },
                  vertical: {
                    root: 'flex flex-col',
                    body: 'p-4 sm:p-6'
                  }
                },
                variant: {
                  outline: {
                    root: 'bg-default ring ring-default',
                    date: 'text-toned',
                    description: 'text-muted'
                  },
                  soft: {
                    root: 'bg-elevated/50',
                    date: 'text-muted',
                    description: 'text-toned'
                  },
                  subtle: {
                    root: 'bg-elevated/50 ring ring-default',
                    date: 'text-muted',
                    description: 'text-toned'
                  },
                  ghost: {
                    date: 'text-toned',
                    description: 'text-muted',
                    header: 'shadow-lg rounded-lg'
                  },
                  naked: {
                    root: 'p-0 sm:p-0',
                    date: 'text-toned',
                    description: 'text-muted',
                    header: 'shadow-lg rounded-lg'
                  }
                },
                to: {
                  true: {
                    root: [
                      'transition'
                    ],
                    image: 'transform transition-transform duration-200 group-hover/blog-post:scale-110',
                    avatar: 'transform transition-transform duration-200 hover:scale-115'
                  }
                },
                image: {
                  true: ''
                }
              },
              compoundVariants: [
                {
                  variant: 'outline',
                  to: true,
                  class: {
                    root: 'hover:bg-elevated/50'
                  }
                },
                {
                  variant: 'soft',
                  to: true,
                  class: {
                    root: 'hover:bg-elevated'
                  }
                },
                {
                  variant: 'subtle',
                  to: true,
                  class: {
                    root: 'hover:bg-elevated hover:ring-accented'
                  }
                },
                {
                  variant: 'ghost',
                  to: true,
                  class: {
                    root: 'hover:bg-elevated/50',
                    header: [
                      'group-hover/blog-post:shadow-none',
                      'transition-all'
                    ]
                  }
                },
                {
                  variant: 'ghost',
                  to: true,
                  orientation: 'vertical',
                  class: {
                    header: 'group-hover/blog-post:rounded-b-none'
                  }
                },
                {
                  variant: 'ghost',
                  to: true,
                  orientation: 'horizontal',
                  class: {
                    header: 'group-hover/blog-post:rounded-r-none'
                  }
                },
                {
                  orientation: 'vertical',
                  image: false,
                  variant: 'naked',
                  class: {
                    body: 'p-0 sm:p-0'
                  }
                }
              ],
              defaultVariants: {
                variant: 'outline'
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
            blogPost: {
              slots: {
                root: 'relative group/blog-post flex flex-col rounded-lg overflow-hidden',
                header: 'relative overflow-hidden aspect-[16/9] w-full pointer-events-none',
                body: 'min-w-0 flex-1 flex flex-col',
                footer: '',
                image: 'object-cover object-top w-full h-full',
                title: 'text-xl text-pretty font-semibold text-highlighted',
                description: 'mt-1 text-base text-pretty',
                authors: 'pt-4 mt-auto flex flex-wrap gap-x-3 gap-y-1.5',
                avatar: '',
                meta: 'flex items-center gap-2 mb-2',
                date: 'text-sm',
                badge: ''
              },
              variants: {
                orientation: {
                  horizontal: {
                    root: 'lg:grid lg:grid-cols-2 lg:items-center gap-x-8',
                    body: 'justify-center p-4 sm:p-6 lg:px-0'
                  },
                  vertical: {
                    root: 'flex flex-col',
                    body: 'p-4 sm:p-6'
                  }
                },
                variant: {
                  outline: {
                    root: 'bg-default ring ring-default',
                    date: 'text-toned',
                    description: 'text-muted'
                  },
                  soft: {
                    root: 'bg-elevated/50',
                    date: 'text-muted',
                    description: 'text-toned'
                  },
                  subtle: {
                    root: 'bg-elevated/50 ring ring-default',
                    date: 'text-muted',
                    description: 'text-toned'
                  },
                  ghost: {
                    date: 'text-toned',
                    description: 'text-muted',
                    header: 'shadow-lg rounded-lg'
                  },
                  naked: {
                    root: 'p-0 sm:p-0',
                    date: 'text-toned',
                    description: 'text-muted',
                    header: 'shadow-lg rounded-lg'
                  }
                },
                to: {
                  true: {
                    root: [
                      'transition'
                    ],
                    image: 'transform transition-transform duration-200 group-hover/blog-post:scale-110',
                    avatar: 'transform transition-transform duration-200 hover:scale-115'
                  }
                },
                image: {
                  true: ''
                }
              },
              compoundVariants: [
                {
                  variant: 'outline',
                  to: true,
                  class: {
                    root: 'hover:bg-elevated/50'
                  }
                },
                {
                  variant: 'soft',
                  to: true,
                  class: {
                    root: 'hover:bg-elevated'
                  }
                },
                {
                  variant: 'subtle',
                  to: true,
                  class: {
                    root: 'hover:bg-elevated hover:ring-accented'
                  }
                },
                {
                  variant: 'ghost',
                  to: true,
                  class: {
                    root: 'hover:bg-elevated/50',
                    header: [
                      'group-hover/blog-post:shadow-none',
                      'transition-all'
                    ]
                  }
                },
                {
                  variant: 'ghost',
                  to: true,
                  orientation: 'vertical',
                  class: {
                    header: 'group-hover/blog-post:rounded-b-none'
                  }
                },
                {
                  variant: 'ghost',
                  to: true,
                  orientation: 'horizontal',
                  class: {
                    header: 'group-hover/blog-post:rounded-r-none'
                  }
                },
                {
                  orientation: 'vertical',
                  image: false,
                  variant: 'naked',
                  class: {
                    body: 'p-0 sm:p-0'
                  }
                }
              ],
              defaultVariants: {
                variant: 'outline'
              }
            }
          }
        })
      ]
    })
    

Expand code

[BannerDisplay a banner at the top of your website to inform users about
important information.](/components/banner)[BlogPostsDisplay a list of blog
posts in a responsive grid layout.](/components/blog-posts)


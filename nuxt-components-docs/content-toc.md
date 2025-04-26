<!-- source: https://ui.nuxt.com/components/content-toc --> # ContentTocPRO

[GitHub](https://github.com/nuxt/ui-
pro/tree/v3/src/runtime/components/content/ContentToc.vue)

A sticky Table of Contents with automatic active anchor link highlighting.

[](/getting-started/content)This component is only available when the
`@nuxt/content` module is installed.

## Usage

Use the `links` prop with the `page?.body?.toc?.links` you get when fetching a
page.

    
    
    <script setup lang="ts">
    const route = useRoute()
    
    const { data: page } = await useAsyncData(route.path, () => queryCollection('content').path(route.path).first())
    if (!page.value) {
      throw createError({ statusCode: 404, statusMessage: 'Page not found', fatal: true })
    }
    </script>
    
    <template>
      <UContentToc :links="page?.body?.toc?.links" />
    </template>
    

### Title

Use the `title` prop to change the title of the Table of Contents.

title

    
    
    <script setup lang="ts">
    const links = ref([
      {
        id: 'usage',
        depth: 2,
        text: 'Usage',
        children: [
          {
            id: 'title',
            depth: 3,
            text: 'Title'
          },
          {
            id: 'color',
            depth: 3,
            text: 'Color'
          },
          {
            id: 'highlight',
            depth: 3,
            text: 'Highlight'
          }
        ]
      },
      {
        id: 'api',
        depth: 2,
        text: 'API',
        children: [
          {
            id: 'props',
            depth: 3,
            text: 'Props'
          },
          {
            id: 'slots',
            depth: 3,
            text: 'Slots'
          }
        ]
      },
      {
        id: 'theme',
        depth: 2,
        text: 'Theme'
      }
    ])
    </script>
    
    <template>
      <UContentToc title="On this page" :links="links" />
    </template>
    

Expand code

### Color

Use the `color` prop to change the color of the links.

color

neutral

    
    
    <script setup lang="ts">
    const links = ref([
      {
        id: 'usage',
        depth: 2,
        text: 'Usage',
        children: [
          {
            id: 'title',
            depth: 3,
            text: 'Title'
          },
          {
            id: 'color',
            depth: 3,
            text: 'Color'
          },
          {
            id: 'highlight',
            depth: 3,
            text: 'Highlight'
          }
        ]
      }
    ])
    </script>
    
    <template>
      <UContentToc color="neutral" :links="links" />
    </template>
    

Expand code

### Highlight

Use the `highlight` prop to display a highlighted border for the active item.

Use the `highlight-color` prop to change the color of the border. It defaults
to the `color` prop.

highlight

true

highlightColor

neutral

color

neutral

    
    
    <script setup lang="ts">
    const links = ref([
      {
        id: 'usage',
        depth: 2,
        text: 'Usage',
        children: [
          {
            id: 'title',
            depth: 3,
            text: 'Title'
          },
          {
            id: 'color',
            depth: 3,
            text: 'Color'
          },
          {
            id: 'highlight',
            depth: 3,
            text: 'Highlight'
          }
        ]
      }
    ])
    </script>
    
    <template>
      <UContentToc highlight highlight-color="neutral" color="neutral" :links="links" />
    </template>
    

Expand code

## Examples

### Within a page

Use the ContentToc component in a page to display the Table of Contents:

pages/[...slug].vue

    
    
    <script setup lang="ts">
    const route = useRoute()
    
    const { data: page } = await useAsyncData(route.path, () => queryCollection('content').path(route.path).first())
    if (!page.value) {
      throw createError({ statusCode: 404, statusMessage: 'Page not found', fatal: true })
    }
    </script>
    
    <template>
      <UPage v-if="page">
        <UPageHeader :title="page.title" />
    
        <UPageBody>
          <ContentRenderer v-if="page.body" :value="page" />
    
          <USeparator v-if="surround?.filter(Boolean).length" />
    
          <UContentSurround :surround="(surround as any)" />
        </UPageBody>
    
        <template v-if="page?.body?.toc?.links?.length" #right>
          <UContentToc :links="page.body.toc.links" />
        </template>
      </UPage>
    </template>
    

## API

### Props

Prop |  Default |  Type   
---|---|---  
`as`| `'nav'`| `any`The element or component this component should render as.  
`trailingIcon`| `appConfig.ui.icons.chevronDown`| ` string`The icon displayed
to collapse the content.  
`title`| `t('contentToc.title')`| ` string`The title of the table of contents.  
`color`| `'primary'`| ` "error" | "primary" | "secondary" | "success" | "info" | "warning" | "neutral"`  
`highlight`| `false`| `boolean`Display a line next to the active link.  
`highlightColor`| `'primary'`| ` "error" | "primary" | "secondary" | "success" | "info" | "warning" | "neutral"`  
`links`| | ` ContentTocLink[]`Show properties

  * `id: string`
  * `text: string`
  * `depth: number`
  * `children?: TocLink[]`
  * `class?: any`

  
`open`| | `boolean`The controlled open state of the collapsible. Can be binded with `v-model`.  
`defaultOpen`| | `boolean`The open state of the collapsible when it is initially rendered.   
Use when you do not need to control its open state.  
`ui`| | ` { root?: ClassNameValue; container?: ClassNameValue; top?: ClassNameValue; bottom?: ClassNameValue; trigger?: ClassNameValue; ... 10 more ...; indicator?: ClassNameValue; }`  
  
### Slots

Slot |  Type   
---|---  
`leading`| `{ open: boolean; }`  
`default`| `{ open: boolean; }`  
`trailing`| `{ open: boolean; }`  
`content`| `{ links: ContentTocLink[]; }`  
`link`| `{ link: ContentTocLink; }`  
`top`| `{ links?: ContentTocLink[] | undefined; }`  
`bottom`| `{ links?: ContentTocLink[] | undefined; }`  
  
### Emits

Event |  Type   
---|---  
`update:open`| `boolean`  
`move`| `string`  
  
## Theme

app.config.ts

    
    
    export default defineAppConfig({
      uiPro: {
        contentToc: {
          slots: {
            root: 'sticky top-(--ui-header-height) bg-default/75 lg:bg-[initial] backdrop-blur -mx-4 px-4 sm:px-6 sm:-mx-6 overflow-y-auto max-h-[calc(100vh-var(--ui-header-height))]',
            container: 'pt-4 sm:pt-6 pb-2.5 sm:pb-4.5 lg:py-8 border-b border-dashed border-default lg:border-0 flex flex-col',
            top: '',
            bottom: 'mt-6 hidden lg:flex lg:flex-col gap-6',
            trigger: 'group text-sm font-semibold flex-1 flex items-center gap-1.5 py-1.5 -mt-1.5 focus-visible:outline-primary',
            title: 'truncate',
            trailing: 'ms-auto inline-flex gap-1.5 items-center',
            trailingIcon: 'size-5 transform transition-transform duration-200 shrink-0 group-data-[state=open]:rotate-180 lg:hidden',
            content: 'data-[state=open]:animate-[collapsible-down_200ms_ease-out] data-[state=closed]:animate-[collapsible-up_200ms_ease-out] overflow-hidden focus:outline-none',
            list: 'min-w-0',
            listWithChildren: 'ms-3',
            item: 'min-w-0',
            itemWithChildren: '',
            link: 'group relative text-sm flex items-center focus-visible:outline-primary py-1',
            linkText: 'truncate',
            indicator: 'absolute ms-2.5 transition-[translate,height] duration-200 h-(--indicator-size) translate-y-(--indicator-position) w-px rounded-full'
          },
          variants: {
            color: {
              primary: '',
              secondary: '',
              success: '',
              info: '',
              warning: '',
              error: '',
              neutral: ''
            },
            highlightColor: {
              primary: {
                indicator: 'bg-primary'
              },
              secondary: {
                indicator: 'bg-secondary'
              },
              success: {
                indicator: 'bg-success'
              },
              info: {
                indicator: 'bg-info'
              },
              warning: {
                indicator: 'bg-warning'
              },
              error: {
                indicator: 'bg-error'
              },
              neutral: {
                indicator: 'bg-inverted'
              }
            },
            active: {
              false: {
                link: [
                  'text-muted hover:text-default',
                  'transition-colors'
                ]
              }
            },
            highlight: {
              true: {
                list: 'ms-2.5 ps-4 border-s border-default',
                item: '-ms-px'
              }
            }
          },
          compoundVariants: [
            {
              color: 'primary',
              active: true,
              class: {
                link: 'text-primary',
                linkLeadingIcon: 'text-primary'
              }
            },
            {
              color: 'neutral',
              active: true,
              class: {
                link: 'text-highlighted',
                linkLeadingIcon: 'text-highlighted'
              }
            }
          ],
          defaultVariants: {
            color: 'primary',
            highlightColor: 'primary'
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
            contentToc: {
              slots: {
                root: 'sticky top-(--ui-header-height) bg-default/75 lg:bg-[initial] backdrop-blur -mx-4 px-4 sm:px-6 sm:-mx-6 overflow-y-auto max-h-[calc(100vh-var(--ui-header-height))]',
                container: 'pt-4 sm:pt-6 pb-2.5 sm:pb-4.5 lg:py-8 border-b border-dashed border-default lg:border-0 flex flex-col',
                top: '',
                bottom: 'mt-6 hidden lg:flex lg:flex-col gap-6',
                trigger: 'group text-sm font-semibold flex-1 flex items-center gap-1.5 py-1.5 -mt-1.5 focus-visible:outline-primary',
                title: 'truncate',
                trailing: 'ms-auto inline-flex gap-1.5 items-center',
                trailingIcon: 'size-5 transform transition-transform duration-200 shrink-0 group-data-[state=open]:rotate-180 lg:hidden',
                content: 'data-[state=open]:animate-[collapsible-down_200ms_ease-out] data-[state=closed]:animate-[collapsible-up_200ms_ease-out] overflow-hidden focus:outline-none',
                list: 'min-w-0',
                listWithChildren: 'ms-3',
                item: 'min-w-0',
                itemWithChildren: '',
                link: 'group relative text-sm flex items-center focus-visible:outline-primary py-1',
                linkText: 'truncate',
                indicator: 'absolute ms-2.5 transition-[translate,height] duration-200 h-(--indicator-size) translate-y-(--indicator-position) w-px rounded-full'
              },
              variants: {
                color: {
                  primary: '',
                  secondary: '',
                  success: '',
                  info: '',
                  warning: '',
                  error: '',
                  neutral: ''
                },
                highlightColor: {
                  primary: {
                    indicator: 'bg-primary'
                  },
                  secondary: {
                    indicator: 'bg-secondary'
                  },
                  success: {
                    indicator: 'bg-success'
                  },
                  info: {
                    indicator: 'bg-info'
                  },
                  warning: {
                    indicator: 'bg-warning'
                  },
                  error: {
                    indicator: 'bg-error'
                  },
                  neutral: {
                    indicator: 'bg-inverted'
                  }
                },
                active: {
                  false: {
                    link: [
                      'text-muted hover:text-default',
                      'transition-colors'
                    ]
                  }
                },
                highlight: {
                  true: {
                    list: 'ms-2.5 ps-4 border-s border-default',
                    item: '-ms-px'
                  }
                }
              },
              compoundVariants: [
                {
                  color: 'primary',
                  active: true,
                  class: {
                    link: 'text-primary',
                    linkLeadingIcon: 'text-primary'
                  }
                },
                {
                  color: 'neutral',
                  active: true,
                  class: {
                    link: 'text-highlighted',
                    linkLeadingIcon: 'text-highlighted'
                  }
                }
              ],
              defaultVariants: {
                color: 'primary',
                highlightColor: 'primary'
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
            contentToc: {
              slots: {
                root: 'sticky top-(--ui-header-height) bg-default/75 lg:bg-[initial] backdrop-blur -mx-4 px-4 sm:px-6 sm:-mx-6 overflow-y-auto max-h-[calc(100vh-var(--ui-header-height))]',
                container: 'pt-4 sm:pt-6 pb-2.5 sm:pb-4.5 lg:py-8 border-b border-dashed border-default lg:border-0 flex flex-col',
                top: '',
                bottom: 'mt-6 hidden lg:flex lg:flex-col gap-6',
                trigger: 'group text-sm font-semibold flex-1 flex items-center gap-1.5 py-1.5 -mt-1.5 focus-visible:outline-primary',
                title: 'truncate',
                trailing: 'ms-auto inline-flex gap-1.5 items-center',
                trailingIcon: 'size-5 transform transition-transform duration-200 shrink-0 group-data-[state=open]:rotate-180 lg:hidden',
                content: 'data-[state=open]:animate-[collapsible-down_200ms_ease-out] data-[state=closed]:animate-[collapsible-up_200ms_ease-out] overflow-hidden focus:outline-none',
                list: 'min-w-0',
                listWithChildren: 'ms-3',
                item: 'min-w-0',
                itemWithChildren: '',
                link: 'group relative text-sm flex items-center focus-visible:outline-primary py-1',
                linkText: 'truncate',
                indicator: 'absolute ms-2.5 transition-[translate,height] duration-200 h-(--indicator-size) translate-y-(--indicator-position) w-px rounded-full'
              },
              variants: {
                color: {
                  primary: '',
                  secondary: '',
                  success: '',
                  info: '',
                  warning: '',
                  error: '',
                  neutral: ''
                },
                highlightColor: {
                  primary: {
                    indicator: 'bg-primary'
                  },
                  secondary: {
                    indicator: 'bg-secondary'
                  },
                  success: {
                    indicator: 'bg-success'
                  },
                  info: {
                    indicator: 'bg-info'
                  },
                  warning: {
                    indicator: 'bg-warning'
                  },
                  error: {
                    indicator: 'bg-error'
                  },
                  neutral: {
                    indicator: 'bg-inverted'
                  }
                },
                active: {
                  false: {
                    link: [
                      'text-muted hover:text-default',
                      'transition-colors'
                    ]
                  }
                },
                highlight: {
                  true: {
                    list: 'ms-2.5 ps-4 border-s border-default',
                    item: '-ms-px'
                  }
                }
              },
              compoundVariants: [
                {
                  color: 'primary',
                  active: true,
                  class: {
                    link: 'text-primary',
                    linkLeadingIcon: 'text-primary'
                  }
                },
                {
                  color: 'neutral',
                  active: true,
                  class: {
                    link: 'text-highlighted',
                    linkLeadingIcon: 'text-highlighted'
                  }
                }
              ],
              defaultVariants: {
                color: 'primary',
                highlightColor: 'primary'
              }
            }
          }
        })
      ]
    })
    

Expand code

[](https://github.com/nuxt/ui-pro/blob/v3/src/theme/content/content-toc.ts
"Compound variants")Some colors in `compoundVariants` are omitted for
readability. Check out the source code on GitHub.

[ContentSurroundA pair of prev and next links to navigate between
pages.](/components/content-surround)[ContextMenuA menu to display actions
when right-clicking on an element.](/components/context-menu)


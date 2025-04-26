<!-- source: https://ui.nuxt.com/components/content-surround --> # ContentSurroundPRO

[GitHub](https://github.com/nuxt/ui-
pro/tree/v3/src/runtime/components/content/ContentSurround.vue)

A pair of prev and next links to navigate between pages.

[](/getting-started/content)This component is only available when the
`@nuxt/content` module is installed.

## Usage

Use the `surround` prop with the `surround` value you get when fetching a page
surround.

[ContentSearchButtonA pre-styled Button to open the ContentSearch
modal.](/components/content-search-button)[ContentTocA sticky Table of
Contents with automatic active anchor link highlighting.](/components/content-
toc)

    
    
    <script setup lang="ts">
    const route = useRoute()
    
    const { data: surround } = await useAsyncData(`${route.path}-surround`, () => {
      return queryCollectionItemSurroundings('content', route.path, {
        fields: ['description']
      })
    })
    </script>
    
    <template>
      <UContentSurround :surround="(surround as any)" />
    </template>
    

### Prev / Next

Use the `prev-icon` and `next-icon` props to customize the buttons
[Icon](/components/icon).

prevIcon

nextIcon

[ContentSearchButtonA pre-styled Button to open the ContentSearch
modal.](/components/content-search-button)[ContentTocA sticky Table of
Contents with customizable slots.](/components/content-toc)

    
    
    <script setup lang="ts">
    const surround = ref([
      {
        title: 'ContentSearchButton',
        path: '/components/content-search-button',
        stem: '3.components/content-search-button',
        description: 'A pre-styled Button to open the ContentSearch modal.'
      },
      {
        title: 'ContentToc',
        path: '/components/content-toc',
        stem: '3.components/content-toc',
        description: 'A sticky Table of Contents with customizable slots.'
      }
    ])
    </script>
    
    <template>
      <UContentSurround
        prev-icon="i-lucide-chevron-left"
        next-icon="i-lucide-chevron-right"
        :surround="surround"
      />
    </template>
    

Expand code

## Examples

### Within a page

Use the ContentSurround component in a page to display the prev and next
links:

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
`as`| `'div'`| `any`The element or component this component should render as.  
`prevIcon`| `appConfig.ui.icons.arrowLeft`| ` string`The icon displayed in the
prev link.  
`nextIcon`| `appConfig.ui.icons.arrowRight`| ` string`The icon displayed in
the next link.  
`surround`| | ` ContentSurroundLink[]`Show properties

  * `description?: string`
  * `icon?: string`
  * `class?: any`
  * `title: string`
  * `path: string`
  * `stem?: string`
  * `children?: ContentNavigationItem[]`
  * `page?: false`

  
`ui`| | ` { root?: ClassNameValue; link?: ClassNameValue; linkLeading?: ClassNameValue; linkLeadingIcon?: ClassNameValue; linkTitle?: ClassNameValue; linkDescription?: ClassNameValue; }`  
  
### Slots

Slot |  Type   
---|---  
`link`| `{ link: ContentSurroundLink; }`  
`link-leading`| `{ link: ContentSurroundLink; }`  
`link-title`| `{ link: ContentSurroundLink; }`  
`link-description`| `{ link: ContentSurroundLink; }`  
  
## Theme

app.config.ts

    
    
    export default defineAppConfig({
      uiPro: {
        contentSurround: {
          slots: {
            root: 'grid grid-cols-1 sm:grid-cols-2 gap-8',
            link: [
              'group block px-6 py-8 rounded-lg border border-default hover:bg-elevated/50 focus-visible:outline-primary',
              'transition-colors'
            ],
            linkLeading: [
              'inline-flex items-center rounded-full p-1.5 bg-elevated group-hover:bg-primary/10 ring ring-accented mb-4 group-hover:ring-primary/50',
              'transition'
            ],
            linkLeadingIcon: [
              'size-5 shrink-0 text-highlighted group-hover:text-primary',
              'transition-[color,translate]'
            ],
            linkTitle: 'font-medium text-[15px] text-highlighted mb-1 truncate',
            linkDescription: 'text-sm text-muted line-clamp-2'
          },
          variants: {
            direction: {
              left: {
                linkLeadingIcon: [
                  'group-active:-translate-x-0.5'
                ]
              },
              right: {
                link: 'text-right',
                linkLeadingIcon: [
                  'group-active:translate-x-0.5'
                ]
              }
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
            contentSurround: {
              slots: {
                root: 'grid grid-cols-1 sm:grid-cols-2 gap-8',
                link: [
                  'group block px-6 py-8 rounded-lg border border-default hover:bg-elevated/50 focus-visible:outline-primary',
                  'transition-colors'
                ],
                linkLeading: [
                  'inline-flex items-center rounded-full p-1.5 bg-elevated group-hover:bg-primary/10 ring ring-accented mb-4 group-hover:ring-primary/50',
                  'transition'
                ],
                linkLeadingIcon: [
                  'size-5 shrink-0 text-highlighted group-hover:text-primary',
                  'transition-[color,translate]'
                ],
                linkTitle: 'font-medium text-[15px] text-highlighted mb-1 truncate',
                linkDescription: 'text-sm text-muted line-clamp-2'
              },
              variants: {
                direction: {
                  left: {
                    linkLeadingIcon: [
                      'group-active:-translate-x-0.5'
                    ]
                  },
                  right: {
                    link: 'text-right',
                    linkLeadingIcon: [
                      'group-active:translate-x-0.5'
                    ]
                  }
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
            contentSurround: {
              slots: {
                root: 'grid grid-cols-1 sm:grid-cols-2 gap-8',
                link: [
                  'group block px-6 py-8 rounded-lg border border-default hover:bg-elevated/50 focus-visible:outline-primary',
                  'transition-colors'
                ],
                linkLeading: [
                  'inline-flex items-center rounded-full p-1.5 bg-elevated group-hover:bg-primary/10 ring ring-accented mb-4 group-hover:ring-primary/50',
                  'transition'
                ],
                linkLeadingIcon: [
                  'size-5 shrink-0 text-highlighted group-hover:text-primary',
                  'transition-[color,translate]'
                ],
                linkTitle: 'font-medium text-[15px] text-highlighted mb-1 truncate',
                linkDescription: 'text-sm text-muted line-clamp-2'
              },
              variants: {
                direction: {
                  left: {
                    linkLeadingIcon: [
                      'group-active:-translate-x-0.5'
                    ]
                  },
                  right: {
                    link: 'text-right',
                    linkLeadingIcon: [
                      'group-active:translate-x-0.5'
                    ]
                  }
                }
              }
            }
          }
        })
      ]
    })
    

Expand code

[ContentSearchButtonA pre-styled Button to open the ContentSearch
modal.](/components/content-search-button)[ContentTocA sticky Table of
Contents with automatic active anchor link highlighting.](/components/content-
toc)


<!-- source: https://ui.nuxt.com/components/page --> # PagePRO

[GitHub](https://github.com/nuxt/ui-
pro/tree/v3/src/runtime/components/Page.vue)

A grid layout for your pages with left and right columns.

## Usage

The Page component helps you create layouts with optional left and right
columns. It's perfect for building documentation sites and other content-
focused pages.

    
    
    <template>
      <UPage>
        <template #left />
    
        <template #right />
      </UPage>
    </template>
    

The page will display as a centered single column layout if no slots are
specified.

## Examples

While these examples use [Nuxt Content](https://content.nuxt.com), the
components can be integrated with any content management system.

### Within a layout

Use the Page component in a layout with the `left` slot to display a
navigation:

layouts/docs.vue

    
    
    <script setup lang="ts">
    import type { ContentNavigationItem } from '@nuxt/content'
    
    const navigation = inject<Ref<ContentNavigationItem[]>>('navigation')
    </script>
    
    <template>
      <UPage>
        <template #left>
          <UPageAside>
            <UContentNavigation :navigation="navigation" />
          </UPageAside>
        </template>
    
        <slot />
      </UPage>
    </template>
    

In this example, we use the `ContentNavigation` component to display the
navigation injected in `app.vue`.

### Within a page

Use the Page component in a page with the `right` slot to display a table of
contents:

pages/[...slug].vue

    
    
    <script setup lang="ts">
    const route = useRoute()
    
    definePageMeta({
      layout: 'docs'
    })
    
    const { data: page } = await useAsyncData(route.path, () => {
      return queryCollection('content').path(route.path).first()
    })
    
    const { data: surround } = await useAsyncData(`${route.path}-surround`, () => {
      return queryCollectionItemSurroundings('content', route.path)
    })
    </script>
    
    <template>
      <UPage>
        <UPageHeader :title="page.title" :description="page.description" />
    
        <UPageBody>
          <ContentRenderer :value="page" />
    
          <USeparator />
    
          <UContentSurround :surround="surround" />
        </UPageBody>
    
        <template #right>
          <UContentToc :links="page.body.toc.links" />
        </template>
      </UPage>
    </template>
    

In this example, we use the `ContentToc` component to display the table of
contents.

## API

### Props

Prop |  Default |  Type   
---|---|---  
`as`| `'div'`| `any`The element or component this component should render as.  
`ui`| | ` { root?: ClassNameValue; left?: ClassNameValue; center?: ClassNameValue; right?: ClassNameValue; }`  
  
### Slots

Slot |  Type   
---|---  
`left`| `{}`  
`default`| `{}`  
`right`| `{}`  
  
## Theme

app.config.ts

    
    
    export default defineAppConfig({
      uiPro: {
        page: {
          slots: {
            root: 'flex flex-col lg:grid lg:grid-cols-10 lg:gap-10',
            left: 'lg:col-span-2',
            center: 'lg:col-span-8',
            right: 'lg:col-span-2 order-first lg:order-last'
          },
          variants: {
            left: {
              true: ''
            },
            right: {
              true: ''
            }
          },
          compoundVariants: [
            {
              left: true,
              right: true,
              class: {
                center: 'lg:col-span-6'
              }
            },
            {
              left: false,
              right: false,
              class: {
                center: 'lg:col-span-10'
              }
            }
          ]
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
            page: {
              slots: {
                root: 'flex flex-col lg:grid lg:grid-cols-10 lg:gap-10',
                left: 'lg:col-span-2',
                center: 'lg:col-span-8',
                right: 'lg:col-span-2 order-first lg:order-last'
              },
              variants: {
                left: {
                  true: ''
                },
                right: {
                  true: ''
                }
              },
              compoundVariants: [
                {
                  left: true,
                  right: true,
                  class: {
                    center: 'lg:col-span-6'
                  }
                },
                {
                  left: false,
                  right: false,
                  class: {
                    center: 'lg:col-span-10'
                  }
                }
              ]
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
            page: {
              slots: {
                root: 'flex flex-col lg:grid lg:grid-cols-10 lg:gap-10',
                left: 'lg:col-span-2',
                center: 'lg:col-span-8',
                right: 'lg:col-span-2 order-first lg:order-last'
              },
              variants: {
                left: {
                  true: ''
                },
                right: {
                  true: ''
                }
              },
              compoundVariants: [
                {
                  left: true,
                  right: true,
                  class: {
                    center: 'lg:col-span-6'
                  }
                },
                {
                  left: false,
                  right: false,
                  class: {
                    center: 'lg:col-span-10'
                  }
                }
              ]
            }
          }
        })
      ]
    })
    

Expand code

[NavigationMenuA list of links that can be displayed horizontally or
vertically.](/components/navigation-menu)[PageAccordionA pre-styled Accordion
to display in your pages.](/components/page-accordion)


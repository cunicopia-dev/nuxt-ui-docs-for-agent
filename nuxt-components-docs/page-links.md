<!-- source: https://ui.nuxt.com/components/page-links --> # PageLinksPRO

[GitHub](https://github.com/nuxt/ui-
pro/tree/v3/src/runtime/components/PageLinks.vue)

A list of links to be displayed in the page.

## Usage

### Links

Use the `links` prop as an array of objects with the following properties:

  * `label: string`
  * `icon?: string`

You can pass any property from the [Link](/components/link#props) component
such as `to`, `target`, etc.

    
    
    <script setup lang="ts">
    import type { PageLink } from '@nuxt/ui-pro'
    
    const links = ref<PageLink[]>([
      {
        label: 'Edit this page',
        icon: 'i-lucide-file-pen',
        to: 'https://github.com/nuxt/ui-pro/tree/v3/docs/content/3.components/page-links.md'
      },
      {
        label: 'Star on GitHub',
        icon: 'i-lucide-star',
        to: 'https://github.com/nuxt/ui'
      },
      {
        label: 'Roadmap',
        icon: 'i-lucide-map',
        to: '/roadmap'
      }
    ])
    </script>
    
    <template>
      <UPageLinks :links="links" />
    </template>
    

### Title

Use the `title` prop to display a title above the links.

title

    
    
    <script setup lang="ts">
    import type { PageLink } from '@nuxt/ui-pro'
    
    const links = ref<PageLink[]>([
      {
        label: 'Edit this page',
        icon: 'i-lucide-file-pen',
        to: 'https://github.com/nuxt/ui-pro/tree/v3/docs/content/3.components/page-links.md'
      },
      {
        label: 'Star on GitHub',
        icon: 'i-lucide-star',
        to: 'https://github.com/nuxt/ui'
      },
      {
        label: 'Roadmap',
        icon: 'i-lucide-map',
        to: '/roadmap'
      }
    ])
    </script>
    
    <template>
      <UPageLinks title="Community" :links="links" />
    </template>
    

## Examples

While these examples use [Nuxt Content](https://content.nuxt.com), the
components can be integrated with any content management system.

### Within a page

Use the PageLinks component in the `bottom` slot of the ContentToc component
to display a list of links below the table of contents.

pages/[...slug].vue

    
    
    <script setup lang="ts">
    import type { PageLink } from '@nuxt/ui-pro'
    
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
    
    const links = computed<PageLink[]>(() => [{
      icon: 'i-lucide-file-pen',
      label: 'Edit this page',
      to: `https://github.com/nuxt/ui/edit/v3/docs/content/${page?.value?.stem}.md`,
      target: '_blank'
    }, {
      icon: 'i-lucide-star',
      label: 'Star on GitHub',
      to: 'https://github.com/nuxt/ui',
      target: '_blank'
    }, {
      label: 'Roadmap',
      icon: 'i-lucide-map',
      to: '/roadmap'
    }])
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
          <UContentToc :links="page.body.toc.links">
            <template #bottom>
              <USeparator type="dashed" />
    
              <UPageLinks title="Community" :links="links" />
            </template>
          </UContentToc>
        </template>
      </UPage>
    </template>
    

## API

### Props

Prop |  Default |  Type   
---|---|---  
`as`| `'nav'`| `any`The element or component this component should render as.  
`title`| | ` string`  
`links`| | ` PageLink[]`Show properties

  * `label: string`
  * `icon?: string`
  * `disabled?: boolean`
  * `class?: any`
  * `as?: any`The element or component this component should render as when not a link. Defaults to `'button'`.
  * `target?: "_blank" | "_parent" | "_self" | "_top" | (string & {}) | null`Where to display the linked URL, as the name for a browsing context.
  * `type?: "reset" | "submit" | "button"`The type of the button when not a link. Defaults to `'button'`.
  * `to?: string | RouteLocationAsRelativeGeneric | RouteLocationAsPathGeneric`Route Location the link should navigate to when clicked on.
  * `active?: boolean`Force the link to be active independent of the current route.
  * `raw?: boolean`When `true`, only styles from `class`, `activeClass`, and `inactiveClass` will be applied.

  
`ui`| | ` { root?: ClassNameValue; title?: ClassNameValue; list?: ClassNameValue; item?: ClassNameValue; link?: ClassNameValue; linkLeadingIcon?: ClassNameValue; linkLabel?: ClassNameValue; linkLabelExternalIcon?: ClassNameValue; }`  
  
### Slots

Slot |  Type   
---|---  
`title`| `{}`  
`link`| `{ link: PageLink; active: boolean; }`  
`link-leading`| `{ link: PageLink; active: boolean; }`  
`link-label`| `{ link: PageLink; active: boolean; }`  
`link-trailing`| `{ link: PageLink; active: boolean; }`  
  
## Theme

app.config.ts

    
    
    export default defineAppConfig({
      uiPro: {
        pageLinks: {
          slots: {
            root: 'flex flex-col gap-3',
            title: 'text-sm font-semibold flex items-center gap-1.5',
            list: 'flex flex-col gap-2',
            item: 'relative',
            link: 'group text-sm flex items-center gap-1.5 focus-visible:outline-primary',
            linkLeadingIcon: 'size-5 shrink-0',
            linkLabel: 'truncate',
            linkLabelExternalIcon: 'size-3 absolute top-0 text-dimmed'
          },
          variants: {
            active: {
              true: {
                link: 'text-primary font-medium'
              },
              false: {
                link: [
                  'text-muted hover:text-default',
                  'transition-colors'
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
            pageLinks: {
              slots: {
                root: 'flex flex-col gap-3',
                title: 'text-sm font-semibold flex items-center gap-1.5',
                list: 'flex flex-col gap-2',
                item: 'relative',
                link: 'group text-sm flex items-center gap-1.5 focus-visible:outline-primary',
                linkLeadingIcon: 'size-5 shrink-0',
                linkLabel: 'truncate',
                linkLabelExternalIcon: 'size-3 absolute top-0 text-dimmed'
              },
              variants: {
                active: {
                  true: {
                    link: 'text-primary font-medium'
                  },
                  false: {
                    link: [
                      'text-muted hover:text-default',
                      'transition-colors'
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
            pageLinks: {
              slots: {
                root: 'flex flex-col gap-3',
                title: 'text-sm font-semibold flex items-center gap-1.5',
                list: 'flex flex-col gap-2',
                item: 'relative',
                link: 'group text-sm flex items-center gap-1.5 focus-visible:outline-primary',
                linkLeadingIcon: 'size-5 shrink-0',
                linkLabel: 'truncate',
                linkLabelExternalIcon: 'size-3 absolute top-0 text-dimmed'
              },
              variants: {
                active: {
                  true: {
                    link: 'text-primary font-medium'
                  },
                  false: {
                    link: [
                      'text-muted hover:text-default',
                      'transition-colors'
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

[PageHeroA responsive hero for your pages.](/components/page-hero)[PageListA
vertical list layout for displaying content in a stacked
format.](/components/page-list)


<!-- source: https://ui.nuxt.com/components/page-anchors --> # PageAnchorsPRO

[GitHub](https://github.com/nuxt/ui-
pro/tree/v3/src/runtime/components/PageAnchors.vue)

A list of anchors to be displayed in the page.

## Usage

### Links

Use the `links` prop as an array of objects with the following properties:

  * `label: string`
  * `icon?: string`

You can pass any property from the [Link](/components/link#props) component
such as `to`, `target`, etc.

    
    
    <script setup lang="ts">
    import type { PageAnchor } from '@nuxt/ui-pro'
    
    const links = ref<PageAnchor[]>([
      {
        label: 'Documentation',
        icon: 'i-lucide-book-open',
        to: '/getting-started'
      },
      {
        label: 'Components',
        icon: 'i-lucide-box',
        to: '/components/app'
      },
      {
        label: 'Roadmap',
        icon: 'i-lucide-map',
        to: '/roadmap'
      },
      {
        label: 'Figma Kit',
        icon: 'i-simple-icons-figma',
        to: 'https://www.figma.com/community/file/1288455405058138934',
        target: '_blank'
      },
      {
        label: 'Releases',
        icon: 'i-simple-icons-github',
        to: 'https://github.com/nuxt/ui/releases',
        target: '_blank'
      }
    ])
    </script>
    
    <template>
      <UPageAnchors :links="links" />
    </template>
    

## Examples

While these examples use [Nuxt Content](https://content.nuxt.com), the
components can be integrated with any content management system.

### Within a layout

Use the PageAnchors component inside the [PageAside](/components/page-aside)
component to display a list of links above the navigation.

layouts/docs.vue

    
    
    <script setup lang="ts">
    import type { PageAnchor } from '@nuxt/ui-pro'
    import type { ContentNavigationItem } from '@nuxt/content'
    
    const navigation = inject<ContentNavigationItem[]>('navigation')
    
    const links: PageAnchor[] = [{
      label: 'Documentation',
      icon: 'i-lucide-book-open',
      to: '/getting-started'
    }, {
      label: 'Components',
      icon: 'i-lucide-box',
      to: '/components/app'
    }, {
      label: 'Roadmap',
      icon: 'i-lucide-map',
      to: '/roadmap'
    }, {
      label: 'Figma Kit',
      icon: 'i-simple-icons-figma',
      to: 'https://www.figma.com/community/file/1288455405058138934',
      target: '_blank'
    }, {
      label: 'Releases',
      icon: 'i-lucide-rocket',
      to: 'https://github.com/nuxt/ui/releases',
      target: '_blank'
    }]
    </script>
    
    <template>
      <UPage>
        <template #left>
          <UPageAside>
            <UPageAnchors :links="links" />
    
            <USeparator type="dashed" />
    
            <UContentNavigation :navigation="navigation" />
          </UPageAside>
        </template>
    
        <slot />
      </UPage>
    </template>
    

## API

### Props

Prop |  Default |  Type   
---|---|---  
`as`| `'nav'`| `any`The element or component this component should render as.  
`links`| | ` PageAnchor[]`Show properties

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

  
`ui`| | ` { root?: ClassNameValue; list?: ClassNameValue; item?: ClassNameValue; link?: ClassNameValue; linkLeading?: ClassNameValue; linkLeadingIcon?: ClassNameValue; linkLabel?: ClassNameValue; linkLabelExternalIcon?: ClassNameValue; }`  
  
### Slots

Slot |  Type   
---|---  
`link`| `{ link: PageAnchor; active: boolean; }`  
`link-leading`| `{ link: PageAnchor; active: boolean; }`  
`link-label`| `{ link: PageAnchor; active: boolean; }`  
`link-trailing`| `{ link: PageAnchor; active: boolean; }`  
  
## Theme

app.config.ts

    
    
    export default defineAppConfig({
      uiPro: {
        pageAnchors: {
          slots: {
            root: '',
            list: '',
            item: 'relative',
            link: 'group text-sm flex items-center gap-1.5 py-1 focus-visible:outline-primary',
            linkLeading: 'rounded-md p-1 inline-flex ring-inset ring',
            linkLeadingIcon: 'size-4 shrink-0',
            linkLabel: 'truncate',
            linkLabelExternalIcon: 'size-3 absolute top-0 text-dimmed'
          },
          variants: {
            active: {
              true: {
                link: 'text-primary font-semibold',
                linkLeading: 'bg-primary ring-primary text-inverted'
              },
              false: {
                link: [
                  'text-muted hover:text-default font-medium',
                  'transition-colors'
                ],
                linkLeading: [
                  'bg-elevated/50 ring-accented text-dimmed group-hover:bg-primary group-hover:ring-primary group-hover:text-inverted',
                  'transition'
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
            pageAnchors: {
              slots: {
                root: '',
                list: '',
                item: 'relative',
                link: 'group text-sm flex items-center gap-1.5 py-1 focus-visible:outline-primary',
                linkLeading: 'rounded-md p-1 inline-flex ring-inset ring',
                linkLeadingIcon: 'size-4 shrink-0',
                linkLabel: 'truncate',
                linkLabelExternalIcon: 'size-3 absolute top-0 text-dimmed'
              },
              variants: {
                active: {
                  true: {
                    link: 'text-primary font-semibold',
                    linkLeading: 'bg-primary ring-primary text-inverted'
                  },
                  false: {
                    link: [
                      'text-muted hover:text-default font-medium',
                      'transition-colors'
                    ],
                    linkLeading: [
                      'bg-elevated/50 ring-accented text-dimmed group-hover:bg-primary group-hover:ring-primary group-hover:text-inverted',
                      'transition'
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
            pageAnchors: {
              slots: {
                root: '',
                list: '',
                item: 'relative',
                link: 'group text-sm flex items-center gap-1.5 py-1 focus-visible:outline-primary',
                linkLeading: 'rounded-md p-1 inline-flex ring-inset ring',
                linkLeadingIcon: 'size-4 shrink-0',
                linkLabel: 'truncate',
                linkLabelExternalIcon: 'size-3 absolute top-0 text-dimmed'
              },
              variants: {
                active: {
                  true: {
                    link: 'text-primary font-semibold',
                    linkLeading: 'bg-primary ring-primary text-inverted'
                  },
                  false: {
                    link: [
                      'text-muted hover:text-default font-medium',
                      'transition-colors'
                    ],
                    linkLeading: [
                      'bg-elevated/50 ring-accented text-dimmed group-hover:bg-primary group-hover:ring-primary group-hover:text-inverted',
                      'transition'
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

[PageAccordionA pre-styled Accordion to display in your
pages.](/components/page-accordion)[PageAsideA sticky aside to display your
page navigation.](/components/page-aside)


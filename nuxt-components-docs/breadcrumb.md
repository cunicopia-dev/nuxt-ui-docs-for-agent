<!-- source: https://ui.nuxt.com/components/breadcrumb --> # Breadcrumb

[GitHub](https://github.com/nuxt/ui/tree/v3/src/runtime/components/Breadcrumb.vue)

A hierarchy of links to navigate through a website.

## Usage

### Items

Use the `items` prop as an array of objects with the following properties:

  * `label?: string`
  * `icon?: string`
  * `avatar?: AvatarProps`
  * `class?: any`
  * `slot?: string`

You can pass any property from the [Link](/components/link#props) component
such as `to`, `target`, etc.

    
    
    <script setup lang="ts">
    import type { BreadcrumbItem } from '@nuxt/ui'
    
    const items = ref<BreadcrumbItem[]>([
      {
        label: 'Home',
        icon: 'i-lucide-house'
      },
      {
        label: 'Components',
        icon: 'i-lucide-box',
        to: '/components'
      },
      {
        label: 'Breadcrumb',
        icon: 'i-lucide-link',
        to: '/components/breadcrumb'
      }
    ])
    </script>
    
    <template>
      <UBreadcrumb :items="items" />
    </template>
    

A `span` is rendered instead of a link when the `to` property is not defined.

### Separator Icon

Use the `separator-icon` prop to customize the [Icon](/components/icon)
between each item. Defaults to `i-lucide-chevron-right`.

separatorIcon

    
    
    <script setup lang="ts">
    import type { BreadcrumbItem } from '@nuxt/ui'
    
    const items = ref<BreadcrumbItem[]>([
      {
        label: 'Home',
        icon: 'i-lucide-house'
      },
      {
        label: 'Components',
        icon: 'i-lucide-box',
        to: '/components'
      },
      {
        label: 'Breadcrumb',
        icon: 'i-lucide-link',
        to: '/components/breadcrumb'
      }
    ])
    </script>
    
    <template>
      <UBreadcrumb separator-icon="i-lucide-arrow-right" :items="items" />
    </template>
    

[](/getting-started/icons/nuxt#theme)You can customize this icon globally in
your `app.config.ts` under `ui.icons.chevronRight` key.

[](/getting-started/icons/vue#theme)You can customize this icon globally in
your `vite.config.ts` under `ui.icons.chevronRight` key.

## Examples

### With separator slot

Use the `#separator` slot to customize the separator between each item.

    
    
    <script setup lang="ts">
    import type { BreadcrumbItem } from '@nuxt/ui'
    
    const items: BreadcrumbItem[] = [
      {
        label: 'Home',
        to: '/'
      },
      {
        label: 'Components',
        to: '/components'
      },
      {
        label: 'Breadcrumb',
        to: '/components/breadcrumb'
      }
    ]
    </script>
    
    <template>
      <UBreadcrumb :items="items">
        <template #separator>
          <span class="mx-2 text-muted">/</span>
        </template>
      </UBreadcrumb>
    </template>
    

### With custom slot

Use the `slot` property to customize a specific item.

You will have access to the following slots:

  * `#{{ item.slot }}`
  * `#{{ item.slot }}-leading`
  * `#{{ item.slot }}-label`
  * `#{{ item.slot }}-trailing`

    
    
    <script setup lang="ts">
    import type { BreadcrumbItem } from '@nuxt/ui'
    
    const items = [
      {
        label: 'Home',
        to: '/'
      },
      {
        slot: 'dropdown' as const,
        icon: 'i-lucide-ellipsis',
        children: [
          {
            label: 'Documentation'
          },
          {
            label: 'Themes'
          },
          {
            label: 'GitHub'
          }
        ]
      },
      {
        label: 'Components',
        to: '/components'
      },
      {
        label: 'Breadcrumb',
        to: '/components/breadcrumb'
      }
    ] satisfies BreadcrumbItem[]
    </script>
    
    <template>
      <UBreadcrumb :items="items">
        <template #dropdown="{ item }">
          <UDropdownMenu :items="item.children">
            <UButton :icon="item.icon" color="neutral" variant="link" class="p-0.5" />
          </UDropdownMenu>
        </template>
      </UBreadcrumb>
    </template>
    

You can also use the `#item`, `#item-leading`, `#item-label` and `#item-
trailing` slots to customize all items.

## API

### Props

Prop |  Default |  Type   
---|---|---  
`as`| `'nav'`| `any`The element or component this component should render as.  
`items`| | ` BreadcrumbItem[]`Show properties

  * `label?: string`
  * `icon?: string`
  * `avatar?: AvatarProps`
  * `slot?: string`
  * `class?: any`
  * `as?: any`The element or component this component should render as when not a link. Defaults to `'button'`.
  * `to?: string | RouteLocationAsRelativeGeneric | RouteLocationAsPathGeneric`Route Location the link should navigate to when clicked on.
  * `type?: "reset" | "submit" | "button"`The type of the button when not a link. Defaults to `'button'`.
  * `disabled?: boolean`
  * `active?: boolean`Force the link to be active independent of the current route.
  * `target?: "_blank" | "_parent" | "_self" | "_top" | (string & {}) | null`Where to display the linked URL, as the name for a browsing context.

  
`separatorIcon`| `appConfig.ui.icons.chevronRight`| ` string`The icon to use
as a separator.  
`labelKey`| `'label'`| ` string`The key used to get the label from the item.  
`ui`| | ` { root?: ClassNameValue; list?: ClassNameValue; item?: ClassNameValue; link?: ClassNameValue; linkLeadingIcon?: ClassNameValue; ... 4 more ...; separatorIcon?: ClassNameValue; }`  
  
### Slots

Slot |  Type   
---|---  
`item`| `{ item: BreadcrumbItem; index: number; active?: boolean | undefined; }`  
`item-leading`| `{ item: BreadcrumbItem; index: number; active?: boolean | undefined; }`  
`item-label`| `{ item: BreadcrumbItem; index: number; active?: boolean | undefined; }`  
`item-trailing`| `{ item: BreadcrumbItem; index: number; active?: boolean | undefined; }`  
`separator`| `any`  
  
## Theme

app.config.ts

    
    
    export default defineAppConfig({
      ui: {
        breadcrumb: {
          slots: {
            root: 'relative min-w-0',
            list: 'flex items-center gap-1.5',
            item: 'flex min-w-0',
            link: 'group relative flex items-center gap-1.5 text-sm min-w-0 focus-visible:outline-primary',
            linkLeadingIcon: 'shrink-0 size-5',
            linkLeadingAvatar: 'shrink-0',
            linkLeadingAvatarSize: '2xs',
            linkLabel: 'truncate',
            separator: 'flex',
            separatorIcon: 'shrink-0 size-5 text-muted'
          },
          variants: {
            active: {
              true: {
                link: 'text-primary font-semibold'
              },
              false: {
                link: 'text-muted font-medium'
              }
            },
            disabled: {
              true: {
                link: 'cursor-not-allowed opacity-75'
              }
            },
            to: {
              true: ''
            }
          },
          compoundVariants: [
            {
              disabled: false,
              active: false,
              to: true,
              class: {
                link: [
                  'hover:text-default',
                  'transition-colors'
                ]
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
          ui: {
            breadcrumb: {
              slots: {
                root: 'relative min-w-0',
                list: 'flex items-center gap-1.5',
                item: 'flex min-w-0',
                link: 'group relative flex items-center gap-1.5 text-sm min-w-0 focus-visible:outline-primary',
                linkLeadingIcon: 'shrink-0 size-5',
                linkLeadingAvatar: 'shrink-0',
                linkLeadingAvatarSize: '2xs',
                linkLabel: 'truncate',
                separator: 'flex',
                separatorIcon: 'shrink-0 size-5 text-muted'
              },
              variants: {
                active: {
                  true: {
                    link: 'text-primary font-semibold'
                  },
                  false: {
                    link: 'text-muted font-medium'
                  }
                },
                disabled: {
                  true: {
                    link: 'cursor-not-allowed opacity-75'
                  }
                },
                to: {
                  true: ''
                }
              },
              compoundVariants: [
                {
                  disabled: false,
                  active: false,
                  to: true,
                  class: {
                    link: [
                      'hover:text-default',
                      'transition-colors'
                    ]
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
          ui: {
            breadcrumb: {
              slots: {
                root: 'relative min-w-0',
                list: 'flex items-center gap-1.5',
                item: 'flex min-w-0',
                link: 'group relative flex items-center gap-1.5 text-sm min-w-0 focus-visible:outline-primary',
                linkLeadingIcon: 'shrink-0 size-5',
                linkLeadingAvatar: 'shrink-0',
                linkLeadingAvatarSize: '2xs',
                linkLabel: 'truncate',
                separator: 'flex',
                separatorIcon: 'shrink-0 size-5 text-muted'
              },
              variants: {
                active: {
                  true: {
                    link: 'text-primary font-semibold'
                  },
                  false: {
                    link: 'text-muted font-medium'
                  }
                },
                disabled: {
                  true: {
                    link: 'cursor-not-allowed opacity-75'
                  }
                },
                to: {
                  true: ''
                }
              },
              compoundVariants: [
                {
                  disabled: false,
                  active: false,
                  to: true,
                  class: {
                    link: [
                      'hover:text-default',
                      'transition-colors'
                    ]
                  }
                }
              ]
            }
          }
        })
      ]
    })
    

Expand code

[BadgeA short text to represent a status or a
category.](/components/badge)[ButtonA button element that can act as a link or
trigger an action.](/components/button)


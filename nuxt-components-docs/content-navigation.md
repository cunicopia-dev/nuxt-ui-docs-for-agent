<!-- source: https://ui.nuxt.com/components/content-navigation --> # ContentNavigationPRO

[GitHub](https://github.com/nuxt/ui-
pro/tree/v3/src/runtime/components/content/ContentNavigation.vue)

An accordion-style navigation component for organizing page links.

[](/getting-started/content)This component is only available when the
`@nuxt/content` module is installed.

## Usage

Use the `navigation` prop with the `navigation` value you get when fetching
the navigation of your app.

    
    
    <script setup lang="ts">
    import type { ContentNavigationItem } from '@nuxt/content'
    
    const navigation = inject<Ref<ContentNavigationItem[]>>('navigation')
    </script>
    
    <template>
      <UContentNavigation :navigation="navigation" highlight />
    </template>
    

### Type

Set the `type` prop to `single` to only allow one item to be open at a time.
Defaults to `multiple`.

type

single

    
    
    <script setup lang="ts">
    const navigation = ref([
      {
        title: 'Guide',
        icon: 'i-lucide-book-open',
        path: '#getting-started',
        children: [
          {
            title: 'Introduction',
            path: '#introduction',
            active: true
          },
          {
            title: 'Installation',
            path: '#installation'
          }
        ]
      },
      {
        title: 'Composables',
        icon: 'i-lucide-database',
        path: '#composables',
        children: [
          {
            title: 'defineShortcuts',
            path: '#defineshortcuts'
          },
          {
            title: 'useModal',
            path: '#usemodal'
          }
        ]
      }
    ])
    </script>
    
    <template>
      <UContentNavigation type="single" />
    </template>
    

Expand code

### Color

Use the `color` prop to change the color of the navigation links.

color

neutral

    
    
    <script setup lang="ts">
    const navigation = ref([
      {
        title: 'Guide',
        icon: 'i-lucide-book-open',
        path: '#getting-started',
        children: [
          {
            title: 'Introduction',
            path: '#introduction',
            active: true
          },
          {
            title: 'Installation',
            path: '#installation'
          }
        ]
      },
      {
        title: 'Composables',
        icon: 'i-lucide-database',
        path: '#composables',
        children: [
          {
            title: 'defineShortcuts',
            path: '#defineshortcuts'
          },
          {
            title: 'useModal',
            path: '#usemodal'
          }
        ]
      }
    ])
    </script>
    
    <template>
      <UContentNavigation color="neutral" />
    </template>
    

Expand code

### Variant

Use the `variant` prop to change the variant of the navigation links.

variant

link

    
    
    <script setup lang="ts">
    const navigation = ref([
      {
        title: 'Guide',
        icon: 'i-lucide-book-open',
        path: '#getting-started',
        children: [
          {
            title: 'Introduction',
            path: '#introduction',
            active: true
          },
          {
            title: 'Installation',
            path: '#installation'
          }
        ]
      },
      {
        title: 'Composables',
        icon: 'i-lucide-database',
        path: '#composables',
        children: [
          {
            title: 'defineShortcuts',
            path: '#defineshortcuts'
          },
          {
            title: 'useModal',
            path: '#usemodal'
          }
        ]
      }
    ])
    </script>
    
    <template>
      <UContentNavigation variant="link" />
    </template>
    

Expand code

### Highlight

Use the `highlight` prop to display a highlighted border for the active link.

Use the `highlight-color` prop to change the color of the border. It defaults
to the `color` prop.

highlight

true

highlightColor

primary

color

primary

variant

pill

    
    
    <script setup lang="ts">
    const navigation = ref([
      {
        title: 'Guide',
        icon: 'i-lucide-book-open',
        path: '#getting-started',
        children: [
          {
            title: 'Introduction',
            path: '#introduction',
            active: true
          },
          {
            title: 'Installation',
            path: '#installation'
          }
        ]
      },
      {
        title: 'Composables',
        icon: 'i-lucide-database',
        path: '#composables',
        children: [
          {
            title: 'defineShortcuts',
            path: '#defineshortcuts'
          },
          {
            title: 'useModal',
            path: '#usemodal'
          }
        ]
      }
    ])
    </script>
    
    <template>
      <UContentNavigation highlight highlight-color="primary" color="primary" variant="pill" />
    </template>
    

Expand code

### Trailing Icon

trailingIcon

    
    
    <script setup lang="ts">
    const navigation = ref([
      {
        title: 'Guide',
        icon: 'i-lucide-book-open',
        path: '#getting-started',
        children: [
          {
            title: 'Introduction',
            path: '#introduction',
            active: true
          },
          {
            title: 'Installation',
            path: '#installation'
          }
        ]
      },
      {
        title: 'Composables',
        icon: 'i-lucide-database',
        path: '#composables',
        children: [
          {
            title: 'defineShortcuts',
            path: '#defineshortcuts'
          },
          {
            title: 'useModal',
            path: '#usemodal'
          }
        ]
      }
    ])
    </script>
    
    <template>
      <UContentNavigation trailing-icon="i-lucide-arrow-up" />
    </template>
    

Expand code

## Examples

### Within a layout

Use the ContentNavigation component inside a [PageAside](/components/page-
aside) component within a layout to display the navigation of the page:

layouts/docs.vue

    
    
    <script setup lang="ts">
    import type { ContentNavigationItem } from '@nuxt/content'
    
    const navigation = inject<Ref<ContentNavigationItem[]>>('navigation')
    </script>
    
    <template>
      <UPage>
        <template #left>
          <UPageAside>
            <UContentNavigation :navigation="navigation" highlight />
          </UPageAside>
        </template>
    
        <slot />
      </UPage>
    </template>
    

### Within a header

Use the ContentNavigation component inside the `content` slot of a
[Header](/components/header) component to display the navigation of the page
on mobile:

components/Header.vue

    
    
    <script setup lang="ts">
    import type { ContentNavigationItem } from '@nuxt/content'
    
    const navigation = inject<Ref<ContentNavigationItem[]>>('navigation')
    </script>
    
    <template>
      <UHeader>
        <template #body>
          <UContentNavigation :navigation="navigation" highlight />
        </template>
      </UHeader>
    </template>
    

## API

### Props

Prop |  Default |  Type   
---|---|---  
`as`| `'nav'`| `any`The element or component this component should render as.  
`defaultOpen`| `void 0`| `boolean`When `true`, the tree will be opened based
on the current route. When `false`, the tree will be closed. When `undefined`
(default), the first item will be opened with `type="single"` and the first
level will be opened with `type="multiple"`.  
`trailingIcon`| `appConfig.ui.icons.chevronDown`| ` string`The icon displayed
to toggle the accordion.  
`color`| `'primary'`| ` "error" | "primary" | "secondary" | "success" | "info" | "warning" | "neutral"`  
`variant`| `'pill'`| ` "link" | "pill"`  
`highlight`| `false`| `boolean`Display a line next to the active link.  
`highlightColor`| `'primary'`| ` "error" | "primary" | "secondary" | "success" | "info" | "warning" | "neutral"`  
`collapsible`| `true`| `boolean`When type is "single", allows closing content
when clicking trigger for an open item. When type is "multiple", this prop has
no effect.  
`level`| `0`| ` number`  
`navigation`| | ` ContentNavigationLink[]`Show properties

  * `icon?: string`
  * `badge?: string | number | BadgeProps`Display a badge on the link. `{ color: 'neutral', variant: 'outline', size: 'sm' }`
  * `target?: "_blank" | "_parent" | "_self" | "_top" | (string & {}) | null`
  * `trailingIcon?: string`
  * `disabled?: boolean`
  * `children?: ContentNavigationLink[]`
  * `defaultOpen?: boolean`
  * `active?: boolean`
  * `class?: any`
  * `title: string`
  * `path: string`
  * `stem?: string`
  * `page?: false`

  
`disabled`| `false`| `boolean`When `true`, prevents the user from interacting
with the accordion and all its items  
`type`| `'multiple'`| ` "multiple" | "single"`Determines whether a "single" or "multiple" items can be selected at a time.This prop will overwrite the inferred type from `modelValue` and `defaultValue`.  
`ui`| | ` { root?: ClassNameValue; content?: ClassNameValue; list?: ClassNameValue; item?: ClassNameValue; listWithChildren?: ClassNameValue; ... 9 more ...; linkTitleExternalIcon?: ClassNameValue; }`  
  
### Slots

Slot |  Type   
---|---  
`link`| `{ link: ContentNavigationLink; active?: boolean | undefined; }`  
`link-leading`| `{ link: ContentNavigationLink; active?: boolean | undefined; }`  
`link-title`| `{ link: ContentNavigationLink; active?: boolean | undefined; }`  
`link-trailing`| `{ link: ContentNavigationLink; active?: boolean | undefined; }`  
  
### Emits

Event |  Type   
---|---  
`update:modelValue`| `string | string[]`  
  
## Theme

app.config.ts

    
    
    export default defineAppConfig({
      uiPro: {
        contentNavigation: {
          slots: {
            root: '',
            content: 'data-[state=open]:animate-[accordion-down_200ms_ease-out] data-[state=closed]:animate-[accordion-up_200ms_ease-out] overflow-hidden focus:outline-none',
            list: 'isolate -mx-2.5 -mt-1.5',
            item: '',
            listWithChildren: 'ms-5 border-s border-default',
            itemWithChildren: 'flex flex-col data-[state=open]:mb-1.5',
            trigger: 'font-semibold',
            link: 'group relative w-full px-2.5 py-1.5 before:inset-y-px before:inset-x-0 flex items-center gap-1.5 text-sm before:absolute before:z-[-1] before:rounded-md focus:outline-none focus-visible:outline-none focus-visible:before:ring-inset focus-visible:before:ring-2',
            linkLeadingIcon: 'shrink-0 size-5',
            linkTrailing: 'ms-auto inline-flex gap-1.5 items-center',
            linkTrailingBadge: 'shrink-0',
            linkTrailingBadgeSize: 'sm',
            linkTrailingIcon: 'size-5 transform transition-transform duration-200 shrink-0 group-data-[state=open]:rotate-180',
            linkTitle: 'truncate',
            linkTitleExternalIcon: 'size-3 align-top text-dimmed'
          },
          variants: {
            color: {
              primary: {
                trigger: 'focus-visible:ring-primary',
                link: 'focus-visible:before:ring-primary'
              },
              secondary: {
                trigger: 'focus-visible:ring-secondary',
                link: 'focus-visible:before:ring-secondary'
              },
              success: {
                trigger: 'focus-visible:ring-success',
                link: 'focus-visible:before:ring-success'
              },
              info: {
                trigger: 'focus-visible:ring-info',
                link: 'focus-visible:before:ring-info'
              },
              warning: {
                trigger: 'focus-visible:ring-warning',
                link: 'focus-visible:before:ring-warning'
              },
              error: {
                trigger: 'focus-visible:ring-error',
                link: 'focus-visible:before:ring-error'
              },
              neutral: {
                trigger: 'focus-visible:ring-inverted',
                link: 'focus-visible:before:ring-inverted'
              }
            },
            highlightColor: {
              primary: '',
              secondary: '',
              success: '',
              info: '',
              warning: '',
              error: '',
              neutral: ''
            },
            variant: {
              pill: '',
              link: ''
            },
            active: {
              true: {
                link: 'font-medium'
              },
              false: {
                link: 'text-muted',
                linkLeadingIcon: 'text-dimmed'
              }
            },
            disabled: {
              true: {
                link: 'cursor-not-allowed opacity-75'
              }
            },
            highlight: {
              true: {}
            },
            level: {
              true: {
                item: 'ps-1.5 -ms-px',
                itemWithChildren: 'ps-1.5 -ms-px'
              }
            }
          },
          compoundVariants: [
            {
              highlight: true,
              level: true,
              class: {
                link: [
                  'after:absolute after:-left-1.5 after:inset-y-0.5 after:block after:w-px after:rounded-full',
                  'after:transition-colors'
                ]
              }
            },
            {
              disabled: false,
              active: false,
              variant: 'pill',
              class: {
                link: [
                  'hover:text-highlighted hover:before:bg-elevated/50 data-[state=open]:text-highlighted',
                  'transition-colors before:transition-colors'
                ],
                linkLeadingIcon: [
                  'group-hover:text-default group-data-[state=open]:text-default',
                  'transition-colors'
                ]
              }
            },
            {
              color: 'primary',
              variant: 'pill',
              active: true,
              class: {
                link: 'text-primary',
                linkLeadingIcon: 'text-primary group-data-[state=open]:text-primary'
              }
            },
            {
              color: 'neutral',
              variant: 'pill',
              active: true,
              class: {
                link: 'text-highlighted',
                linkLeadingIcon: 'text-highlighted group-data-[state=open]:text-highlighted'
              }
            },
            {
              variant: 'pill',
              active: true,
              highlight: false,
              class: {
                link: 'before:bg-elevated'
              }
            },
            {
              variant: 'pill',
              active: true,
              highlight: true,
              class: {
                link: [
                  'hover:before:bg-elevated/50',
                  'before:transition-colors'
                ]
              }
            },
            {
              disabled: false,
              active: false,
              variant: 'link',
              class: {
                link: [
                  'hover:text-highlighted data-[state=open]:text-highlighted',
                  'transition-colors'
                ],
                linkLeadingIcon: [
                  'group-hover:text-default group-data-[state=open]:text-default',
                  'transition-colors'
                ]
              }
            },
            {
              color: 'primary',
              variant: 'link',
              active: true,
              class: {
                link: 'text-primary',
                linkLeadingIcon: 'text-primary group-data-[state=open]:text-primary'
              }
            },
            {
              color: 'neutral',
              variant: 'link',
              active: true,
              class: {
                link: 'text-highlighted',
                linkLeadingIcon: 'text-highlighted group-data-[state=open]:text-highlighted'
              }
            },
            {
              highlightColor: 'primary',
              highlight: true,
              level: true,
              active: true,
              class: {
                link: 'after:bg-primary'
              }
            },
            {
              highlightColor: 'neutral',
              highlight: true,
              level: true,
              active: true,
              class: {
                link: 'after:bg-inverted'
              }
            }
          ],
          defaultVariants: {
            color: 'primary',
            highlightColor: 'primary',
            variant: 'pill'
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
            contentNavigation: {
              slots: {
                root: '',
                content: 'data-[state=open]:animate-[accordion-down_200ms_ease-out] data-[state=closed]:animate-[accordion-up_200ms_ease-out] overflow-hidden focus:outline-none',
                list: 'isolate -mx-2.5 -mt-1.5',
                item: '',
                listWithChildren: 'ms-5 border-s border-default',
                itemWithChildren: 'flex flex-col data-[state=open]:mb-1.5',
                trigger: 'font-semibold',
                link: 'group relative w-full px-2.5 py-1.5 before:inset-y-px before:inset-x-0 flex items-center gap-1.5 text-sm before:absolute before:z-[-1] before:rounded-md focus:outline-none focus-visible:outline-none focus-visible:before:ring-inset focus-visible:before:ring-2',
                linkLeadingIcon: 'shrink-0 size-5',
                linkTrailing: 'ms-auto inline-flex gap-1.5 items-center',
                linkTrailingBadge: 'shrink-0',
                linkTrailingBadgeSize: 'sm',
                linkTrailingIcon: 'size-5 transform transition-transform duration-200 shrink-0 group-data-[state=open]:rotate-180',
                linkTitle: 'truncate',
                linkTitleExternalIcon: 'size-3 align-top text-dimmed'
              },
              variants: {
                color: {
                  primary: {
                    trigger: 'focus-visible:ring-primary',
                    link: 'focus-visible:before:ring-primary'
                  },
                  secondary: {
                    trigger: 'focus-visible:ring-secondary',
                    link: 'focus-visible:before:ring-secondary'
                  },
                  success: {
                    trigger: 'focus-visible:ring-success',
                    link: 'focus-visible:before:ring-success'
                  },
                  info: {
                    trigger: 'focus-visible:ring-info',
                    link: 'focus-visible:before:ring-info'
                  },
                  warning: {
                    trigger: 'focus-visible:ring-warning',
                    link: 'focus-visible:before:ring-warning'
                  },
                  error: {
                    trigger: 'focus-visible:ring-error',
                    link: 'focus-visible:before:ring-error'
                  },
                  neutral: {
                    trigger: 'focus-visible:ring-inverted',
                    link: 'focus-visible:before:ring-inverted'
                  }
                },
                highlightColor: {
                  primary: '',
                  secondary: '',
                  success: '',
                  info: '',
                  warning: '',
                  error: '',
                  neutral: ''
                },
                variant: {
                  pill: '',
                  link: ''
                },
                active: {
                  true: {
                    link: 'font-medium'
                  },
                  false: {
                    link: 'text-muted',
                    linkLeadingIcon: 'text-dimmed'
                  }
                },
                disabled: {
                  true: {
                    link: 'cursor-not-allowed opacity-75'
                  }
                },
                highlight: {
                  true: {}
                },
                level: {
                  true: {
                    item: 'ps-1.5 -ms-px',
                    itemWithChildren: 'ps-1.5 -ms-px'
                  }
                }
              },
              compoundVariants: [
                {
                  highlight: true,
                  level: true,
                  class: {
                    link: [
                      'after:absolute after:-left-1.5 after:inset-y-0.5 after:block after:w-px after:rounded-full',
                      'after:transition-colors'
                    ]
                  }
                },
                {
                  disabled: false,
                  active: false,
                  variant: 'pill',
                  class: {
                    link: [
                      'hover:text-highlighted hover:before:bg-elevated/50 data-[state=open]:text-highlighted',
                      'transition-colors before:transition-colors'
                    ],
                    linkLeadingIcon: [
                      'group-hover:text-default group-data-[state=open]:text-default',
                      'transition-colors'
                    ]
                  }
                },
                {
                  color: 'primary',
                  variant: 'pill',
                  active: true,
                  class: {
                    link: 'text-primary',
                    linkLeadingIcon: 'text-primary group-data-[state=open]:text-primary'
                  }
                },
                {
                  color: 'neutral',
                  variant: 'pill',
                  active: true,
                  class: {
                    link: 'text-highlighted',
                    linkLeadingIcon: 'text-highlighted group-data-[state=open]:text-highlighted'
                  }
                },
                {
                  variant: 'pill',
                  active: true,
                  highlight: false,
                  class: {
                    link: 'before:bg-elevated'
                  }
                },
                {
                  variant: 'pill',
                  active: true,
                  highlight: true,
                  class: {
                    link: [
                      'hover:before:bg-elevated/50',
                      'before:transition-colors'
                    ]
                  }
                },
                {
                  disabled: false,
                  active: false,
                  variant: 'link',
                  class: {
                    link: [
                      'hover:text-highlighted data-[state=open]:text-highlighted',
                      'transition-colors'
                    ],
                    linkLeadingIcon: [
                      'group-hover:text-default group-data-[state=open]:text-default',
                      'transition-colors'
                    ]
                  }
                },
                {
                  color: 'primary',
                  variant: 'link',
                  active: true,
                  class: {
                    link: 'text-primary',
                    linkLeadingIcon: 'text-primary group-data-[state=open]:text-primary'
                  }
                },
                {
                  color: 'neutral',
                  variant: 'link',
                  active: true,
                  class: {
                    link: 'text-highlighted',
                    linkLeadingIcon: 'text-highlighted group-data-[state=open]:text-highlighted'
                  }
                },
                {
                  highlightColor: 'primary',
                  highlight: true,
                  level: true,
                  active: true,
                  class: {
                    link: 'after:bg-primary'
                  }
                },
                {
                  highlightColor: 'neutral',
                  highlight: true,
                  level: true,
                  active: true,
                  class: {
                    link: 'after:bg-inverted'
                  }
                }
              ],
              defaultVariants: {
                color: 'primary',
                highlightColor: 'primary',
                variant: 'pill'
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
            contentNavigation: {
              slots: {
                root: '',
                content: 'data-[state=open]:animate-[accordion-down_200ms_ease-out] data-[state=closed]:animate-[accordion-up_200ms_ease-out] overflow-hidden focus:outline-none',
                list: 'isolate -mx-2.5 -mt-1.5',
                item: '',
                listWithChildren: 'ms-5 border-s border-default',
                itemWithChildren: 'flex flex-col data-[state=open]:mb-1.5',
                trigger: 'font-semibold',
                link: 'group relative w-full px-2.5 py-1.5 before:inset-y-px before:inset-x-0 flex items-center gap-1.5 text-sm before:absolute before:z-[-1] before:rounded-md focus:outline-none focus-visible:outline-none focus-visible:before:ring-inset focus-visible:before:ring-2',
                linkLeadingIcon: 'shrink-0 size-5',
                linkTrailing: 'ms-auto inline-flex gap-1.5 items-center',
                linkTrailingBadge: 'shrink-0',
                linkTrailingBadgeSize: 'sm',
                linkTrailingIcon: 'size-5 transform transition-transform duration-200 shrink-0 group-data-[state=open]:rotate-180',
                linkTitle: 'truncate',
                linkTitleExternalIcon: 'size-3 align-top text-dimmed'
              },
              variants: {
                color: {
                  primary: {
                    trigger: 'focus-visible:ring-primary',
                    link: 'focus-visible:before:ring-primary'
                  },
                  secondary: {
                    trigger: 'focus-visible:ring-secondary',
                    link: 'focus-visible:before:ring-secondary'
                  },
                  success: {
                    trigger: 'focus-visible:ring-success',
                    link: 'focus-visible:before:ring-success'
                  },
                  info: {
                    trigger: 'focus-visible:ring-info',
                    link: 'focus-visible:before:ring-info'
                  },
                  warning: {
                    trigger: 'focus-visible:ring-warning',
                    link: 'focus-visible:before:ring-warning'
                  },
                  error: {
                    trigger: 'focus-visible:ring-error',
                    link: 'focus-visible:before:ring-error'
                  },
                  neutral: {
                    trigger: 'focus-visible:ring-inverted',
                    link: 'focus-visible:before:ring-inverted'
                  }
                },
                highlightColor: {
                  primary: '',
                  secondary: '',
                  success: '',
                  info: '',
                  warning: '',
                  error: '',
                  neutral: ''
                },
                variant: {
                  pill: '',
                  link: ''
                },
                active: {
                  true: {
                    link: 'font-medium'
                  },
                  false: {
                    link: 'text-muted',
                    linkLeadingIcon: 'text-dimmed'
                  }
                },
                disabled: {
                  true: {
                    link: 'cursor-not-allowed opacity-75'
                  }
                },
                highlight: {
                  true: {}
                },
                level: {
                  true: {
                    item: 'ps-1.5 -ms-px',
                    itemWithChildren: 'ps-1.5 -ms-px'
                  }
                }
              },
              compoundVariants: [
                {
                  highlight: true,
                  level: true,
                  class: {
                    link: [
                      'after:absolute after:-left-1.5 after:inset-y-0.5 after:block after:w-px after:rounded-full',
                      'after:transition-colors'
                    ]
                  }
                },
                {
                  disabled: false,
                  active: false,
                  variant: 'pill',
                  class: {
                    link: [
                      'hover:text-highlighted hover:before:bg-elevated/50 data-[state=open]:text-highlighted',
                      'transition-colors before:transition-colors'
                    ],
                    linkLeadingIcon: [
                      'group-hover:text-default group-data-[state=open]:text-default',
                      'transition-colors'
                    ]
                  }
                },
                {
                  color: 'primary',
                  variant: 'pill',
                  active: true,
                  class: {
                    link: 'text-primary',
                    linkLeadingIcon: 'text-primary group-data-[state=open]:text-primary'
                  }
                },
                {
                  color: 'neutral',
                  variant: 'pill',
                  active: true,
                  class: {
                    link: 'text-highlighted',
                    linkLeadingIcon: 'text-highlighted group-data-[state=open]:text-highlighted'
                  }
                },
                {
                  variant: 'pill',
                  active: true,
                  highlight: false,
                  class: {
                    link: 'before:bg-elevated'
                  }
                },
                {
                  variant: 'pill',
                  active: true,
                  highlight: true,
                  class: {
                    link: [
                      'hover:before:bg-elevated/50',
                      'before:transition-colors'
                    ]
                  }
                },
                {
                  disabled: false,
                  active: false,
                  variant: 'link',
                  class: {
                    link: [
                      'hover:text-highlighted data-[state=open]:text-highlighted',
                      'transition-colors'
                    ],
                    linkLeadingIcon: [
                      'group-hover:text-default group-data-[state=open]:text-default',
                      'transition-colors'
                    ]
                  }
                },
                {
                  color: 'primary',
                  variant: 'link',
                  active: true,
                  class: {
                    link: 'text-primary',
                    linkLeadingIcon: 'text-primary group-data-[state=open]:text-primary'
                  }
                },
                {
                  color: 'neutral',
                  variant: 'link',
                  active: true,
                  class: {
                    link: 'text-highlighted',
                    linkLeadingIcon: 'text-highlighted group-data-[state=open]:text-highlighted'
                  }
                },
                {
                  highlightColor: 'primary',
                  highlight: true,
                  level: true,
                  active: true,
                  class: {
                    link: 'after:bg-primary'
                  }
                },
                {
                  highlightColor: 'neutral',
                  highlight: true,
                  level: true,
                  active: true,
                  class: {
                    link: 'after:bg-inverted'
                  }
                }
              ],
              defaultVariants: {
                color: 'primary',
                highlightColor: 'primary',
                variant: 'pill'
              }
            }
          }
        })
      ]
    })
    

Expand code

[](https://github.com/nuxt/ui-pro/blob/v3/src/theme/content/content-
navigation.ts "Compound variants")Some colors in `compoundVariants` are
omitted for readability. Check out the source code on GitHub.

[ContainerA container lets you center and constrain the width of your
content.](/components/container)[ContentSearchA ready to use CommandPalette to
add to your documentation.](/components/content-search)


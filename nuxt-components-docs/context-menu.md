<!-- source: https://ui.nuxt.com/components/context-menu --> # ContextMenu

[ContextMenu](https://reka-ui.com/docs/components/context-
menu)[GitHub](https://github.com/nuxt/ui/tree/v3/src/runtime/components/ContextMenu.vue)

A menu to display actions when right-clicking on an element.

## Usage

Use anything you like in the default slot of the ContextMenu, and right-click
on it to display the menu.

### Items

Use the `items` prop as an array of objects with the following properties:

  * `label?: string`
  * `icon?: string`
  * `color?: string`
  * `avatar?: AvatarProps`
  * `kbds?: string[] | KbdProps[]`
  * `type?: "link" | "label" | "separator" | "checkbox"`
  * `color?: "error" | "primary" | "secondary" | "success" | "info" | "warning" | "neutral"`
  * `checked?: boolean`
  * `disabled?: boolean`
  * `class?: any`
  * `slot?: string`
  * `onSelect?(e: Event): void`
  * `onUpdateChecked?(checked: boolean): void`
  * `children?: ContextMenuItem[] | ContextMenuItem[][]`

You can pass any property from the [Link](/components/link#props) component
such as `to`, `target`, etc.

Right click here

    
    
    <script setup lang="ts">
    import type { ContextMenuItem } from '@nuxt/ui'
    
    const items = ref<ContextMenuItem[][]>([
      [
        {
          label: 'Appearance',
          children: [
            {
              label: 'System',
              icon: 'i-lucide-monitor'
            },
            {
              label: 'Light',
              icon: 'i-lucide-sun'
            },
            {
              label: 'Dark',
              icon: 'i-lucide-moon'
            }
          ]
        }
      ],
      [
        {
          label: 'Show Sidebar',
          kbds: ['meta', 's']
        },
        {
          label: 'Show Toolbar',
          kbds: ['shift', 'meta', 'd']
        },
        {
          label: 'Collapse Pinned Tabs',
          disabled: true
        }
      ],
      [
        {
          label: 'Refresh the Page'
        },
        {
          label: 'Clear Cookies and Refresh'
        },
        {
          label: 'Clear Cache and Refresh'
        },
        {
          type: 'separator'
        },
        {
          label: 'Developer',
          children: [
            [
              {
                label: 'View Source',
                kbds: ['meta', 'shift', 'u']
              },
              {
                label: 'Developer Tools',
                kbds: ['option', 'meta', 'i']
              },
              {
                label: 'Inspect Elements',
                kbds: ['option', 'meta', 'c']
              }
            ],
            [
              {
                label: 'JavaScript Console',
                kbds: ['option', 'meta', 'j']
              }
            ]
          ]
        }
      ]
    ])
    </script>
    
    <template>
      <UContextMenu
        :items="items"
        :ui="{
          content: 'w-48'
        }"
      >
        <div
          class="flex items-center justify-center rounded-md border border-dashed border-accented text-sm aspect-video w-72"
        >
          Right click here
        </div>
      </UContextMenu>
    </template>
    

Expand code

You can also pass an array of arrays to the `items` prop to create separated
groups of items.

Each item can take a `children` array of objects with the same properties as
the `items` prop to create a nested menu which can be controlled using the
`open`, `defaultOpen` and `content` properties.

### Size

Use the `size` prop to change the size of the ContextMenu.

size

xl

Right click here

    
    
    <script setup lang="ts">
    import type { ContextMenuItem } from '@nuxt/ui'
    
    const items = ref<ContextMenuItem[]>([
      {
        label: 'System',
        icon: 'i-lucide-monitor'
      },
      {
        label: 'Light',
        icon: 'i-lucide-sun'
      },
      {
        label: 'Dark',
        icon: 'i-lucide-moon'
      }
    ])
    </script>
    
    <template>
      <UContextMenu
        size="xl"
        :items="items"
        :ui="{
          content: 'w-48'
        }"
      >
        <div
          class="flex items-center justify-center rounded-md border border-dashed border-accented text-sm aspect-video w-72"
        >
          Right click here
        </div>
      </UContextMenu>
    </template>
    

### Disabled

Use the `disabled` prop to disable the ContextMenu.

disabled

true

Right click here

    
    
    <script setup lang="ts">
    import type { ContextMenuItem } from '@nuxt/ui'
    
    const items = ref<ContextMenuItem[]>([
      {
        label: 'System',
        icon: 'i-lucide-monitor'
      },
      {
        label: 'Light',
        icon: 'i-lucide-sun'
      },
      {
        label: 'Dark',
        icon: 'i-lucide-moon'
      }
    ])
    </script>
    
    <template>
      <UContextMenu
        disabled
        :items="items"
        :ui="{
          content: 'w-48'
        }"
      >
        <div
          class="flex items-center justify-center rounded-md border border-dashed border-accented text-sm aspect-video w-72"
        >
          Right click here
        </div>
      </UContextMenu>
    </template>
    

## Examples

### With checkbox items

You can use the `type` property with `checkbox` and use the `checked` /
`onUpdateChecked` properties to control the checked state of the item.

Right click here

    
    
    <script setup lang="ts">
    import type { ContextMenuItem } from '@nuxt/ui'
    
    const showSidebar = ref(true)
    const showToolbar = ref(false)
    
    const items = computed<ContextMenuItem[]>(() => [{
      label: 'View',
      type: 'label' as const
    }, {
      type: 'separator' as const
    }, {
      label: 'Show Sidebar',
      type: 'checkbox' as const,
      checked: showSidebar.value,
      onUpdateChecked(checked: boolean) {
        showSidebar.value = checked
      },
      onSelect(e: Event) {
        e.preventDefault()
      }
    }, {
      label: 'Show Toolbar',
      type: 'checkbox' as const,
      checked: showToolbar.value,
      onUpdateChecked(checked: boolean) {
        showToolbar.value = checked
      }
    }, {
      label: 'Collapse Pinned Tabs',
      type: 'checkbox' as const,
      disabled: true
    }])
    </script>
    
    <template>
      <UContextMenu :items="items" :ui="{ content: 'w-48' }">
        <div class="flex items-center justify-center rounded-md border border-dashed border-accented text-sm aspect-video w-72">
          Right click here
        </div>
      </UContextMenu>
    </template>
    

Expand code

To ensure reactivity for the `checked` state of items, it's recommended to
wrap your `items` array inside a `computed`.

### With color items

You can use the `color` property to highlight certain items with a color.

Right click here

    
    
    <script setup lang="ts">
    import type { ContextMenuItem } from '@nuxt/ui'
    
    const items: ContextMenuItem[][] = [
      [
        {
          label: 'View',
          icon: 'i-lucide-eye'
        },
        {
          label: 'Copy',
          icon: 'i-lucide-copy'
        },
        {
          label: 'Edit',
          icon: 'i-lucide-pencil'
        }
      ],
      [
        {
          label: 'Delete',
          color: 'error' as const,
          icon: 'i-lucide-trash'
        }
      ]
    ]
    </script>
    
    <template>
      <UContextMenu :items="items" :ui="{ content: 'w-48' }">
        <div class="flex items-center justify-center rounded-md border border-dashed border-accented text-sm aspect-video w-72">
          Right click here
        </div>
      </UContextMenu>
    </template>
    

### With custom slot

Use the `slot` property to customize a specific item.

You will have access to the following slots:

  * `#{{ item.slot }}`
  * `#{{ item.slot }}-leading`
  * `#{{ item.slot }}-label`
  * `#{{ item.slot }}-trailing`

Right click here

    
    
    <script setup lang="ts">
    import type { ContextMenuItem } from '@nuxt/ui'
    
    const loading = ref(true)
    
    const items = [
      {
        label: 'Refresh the Page',
        slot: 'refresh' as const
      },
      {
        label: 'Clear Cookies and Refresh'
      },
      {
        label: 'Clear Cache and Refresh'
      }
    ] satisfies ContextMenuItem[]
    </script>
    
    <template>
      <UContextMenu :items="items" :ui="{ content: 'w-48' }">
        <div class="flex items-center justify-center rounded-md border border-dashed border-accented text-sm aspect-video w-72">
          Right click here
        </div>
    
        <template #refresh-label>
          {{ loading ? 'Refreshing...' : 'Refresh the Page' }}
        </template>
    
        <template #refresh-trailing>
          <UIcon v-if="loading" name="i-lucide-refresh-cw" class="shrink-0 size-5 text-primary animate-spin" />
        </template>
      </UContextMenu>
    </template>
    

You can also use the `#item`, `#item-leading`, `#item-label` and `#item-
trailing` slots to customize all items.

### Extract shortcuts

When you have some items with `kbds` property (displaying some
[Kbd](/components/kbd)), you can easily make them work with the
[defineShortcuts](/composables/define-shortcuts) composable.

Inside the `defineShortcuts` composable, there is an `extractShortcuts`
utility that will extract the shortcuts recursively from the items and return
an object that you can pass to `defineShortcuts`. It will automatically call
the `select` function of the item when the shortcut is pressed.

    
    
    <script setup lang="ts">
    const items = [
      [{
        label: 'Show Sidebar',
        kbds: ['meta', 'S'],
        onSelect() {
          console.log('Show Sidebar clicked')
        }
      }, {
        label: 'Show Toolbar',
        kbds: ['shift', 'meta', 'D'],
        onSelect() {
          console.log('Show Toolbar clicked')
        }
      }, {
        label: 'Collapse Pinned Tabs',
        disabled: true
      }], [{
        label: 'Refresh the Page'
      }, {
        label: 'Clear Cookies and Refresh'
      }, {
        label: 'Clear Cache and Refresh'
      }, {
        type: 'separator' as const
      }, {
        label: 'Developer',
        children: [[{
          label: 'View Source',
          kbds: ['option', 'meta', 'U'],
          onSelect() {
            console.log('View Source clicked')
          }
        }, {
          label: 'Developer Tools',
          kbds: ['option', 'meta', 'I'],
          onSelect() {
            console.log('Developer Tools clicked')
          }
        }], [{
          label: 'Inspect Elements',
          kbds: ['option', 'meta', 'C'],
          onSelect() {
            console.log('Inspect Elements clicked')
          }
        }], [{
          label: 'JavaScript Console',
          kbds: ['option', 'meta', 'J'],
          onSelect() {
            console.log('JavaScript Console clicked')
          }
        }]]
      }]
    ]
    
    defineShortcuts(extractShortcuts(items))
    </script>
    

In this example, ` ``S`, `⇧`` ``D`, `⌥`` ``U`, `⌥`` ``I`, `⌥`` ``C` and `⌥``
``J` would trigger the `select` function of the corresponding item.

## API

### Props

Prop |  Default |  Type   
---|---|---  
`size`| `'md'`| ` "sm" | "md" | "xs" | "lg" | "xl"`  
`items`| | ` ContextMenuItem[] | ContextMenuItem[][]`Show properties

  * `label?: string`
  * `icon?: string`
  * `color?: "error" | "primary" | "secondary" | "success" | "info" | "warning" | "neutral"`
  * `avatar?: AvatarProps`
  * `content?: (ContextMenuContentProps & Partial<EmitsToProps<MenuContentEmits>>)`
  * `kbds?: (string )[] | KbdProps[] | undefined`
  * `type?: "label" | "separator" | "link" | "checkbox"`The item type. Defaults to `'link'`.
  * `slot?: string`
  * `loading?: boolean`
  * `disabled?: boolean`
  * `checked?: boolean`
  * `open?: boolean`
  * `defaultOpen?: boolean`
  * `children?: ArrayOrNested<ContextMenuItem>`
  * `onSelect?: ((e: Event) => void)`
  * `onUpdateChecked?: ((checked: boolean) => void)`
  * `class?: any`
  * `to?: string | RouteLocationAsRelativeGeneric | RouteLocationAsPathGeneric`Route Location the link should navigate to when clicked on.
  * `as?: any`The element or component this component should render as when not a link. Defaults to `'button'`.
  * `active?: boolean`Force the link to be active independent of the current route.
  * `target?: "_blank" | "_parent" | "_self" | "_top" | (string & {}) | null`Where to display the linked URL, as the name for a browsing context.

  
`checkedIcon`| `appConfig.ui.icons.check`| ` string`The icon displayed when an
item is checked.  
`loadingIcon`| `appConfig.ui.icons.loading`| ` string`The icon displayed when
an item is loading.  
`externalIcon`| `true`| ` string | false | true`The icon displayed when the item is an external link. Set to `false` to hide the external icon.  
`content`| | ` ContextMenuContentProps & Partial<EmitsToProps<MenuContentEmits>>`The content of the menu.Show properties

  * `alignOffset?: number`An offset in pixels from the `start` or `end` alignment options. Defaults to `0`.
  * `avoidCollisions?: boolean`When `true`, overrides the side and align preferences to prevent collisions with boundary edges. Defaults to `true`.
  * `collisionBoundary?: Element | (Element | null)[] | null`The element used as the collision boundary. By default this is the viewport, though you can provide additional element(s) to be included in this check. Defaults to `[]`.
  * `collisionPadding?: number | Partial<Record<"top" | "right" | "bottom" | "left", number>>`The distance in pixels from the boundary edges where collision detection should occur. Accepts a number (same for all sides), or a partial padding object, for example: { top: 20, left: 20 }. Defaults to `0`.
  * `sticky?: "partial" | "always"`The sticky behavior on the align axis. `partial` will keep the content in the boundary as long as the trigger is at least partially in the boundary whilst "always" will keep the content in the boundary regardless. Defaults to `"partial"`.
  * `hideWhenDetached?: boolean`Whether to hide the content when the trigger becomes fully occluded. Defaults to `false`.
  * `positionStrategy?: "fixed" | "absolute"`The type of CSS position property to use.
  * `disableUpdateOnLayoutShift?: boolean`Whether to disable the update position for the content when the layout shifted. Defaults to `false`.
  * `prioritizePosition?: boolean`Force content to be position within the viewport.Might overlap the reference element, which may not be desired. Defaults to `false`.
  * `reference?: ReferenceElement`The custom element or virtual element that will be set as the reference to position the floating element.If provided, it will replace the default anchor element.
  * `loop?: boolean`When `true`, keyboard navigation will loop from last item to first, and vice versa. Defaults to `false`.
  * `onEscapeKeyDown?: ((event: KeyboardEvent) => void)`
  * `onPointerDownOutside?: ((event: PointerDownOutsideEvent) => void)`
  * `onFocusOutside?: ((event: FocusOutsideEvent) => void)`
  * `onInteractOutside?: ((event: PointerDownOutsideEvent | FocusOutsideEvent) => void)`
  * `onCloseAutoFocus?: ((event: Event) => void)`

  
`portal`| `true`| ` string | false | true | HTMLElement`Render the menu in a portal.  
`labelKey`| `'label'`| ` string | number`The key used to get the label from the item.  
`disabled`| | `boolean`  
`modal`| `true`| `boolean`The modality of the dropdown menu.When set to
`true`, interaction with outside elements will be disabled and only menu
content will be visible to screen readers.  
`ui`| | ` { content?: ClassNameValue; group?: ClassNameValue; label?: ClassNameValue; separator?: ClassNameValue; item?: ClassNameValue; ... 8 more ...; itemLabelExternalIcon?: ClassNameValue; }`  
  
### Slots

Slot |  Type   
---|---  
`default`| `{}`  
`item`| `{ item: ContextMenuItem; active?: boolean | undefined; index: number; }`  
`item-leading`| `{ item: ContextMenuItem; active?: boolean | undefined; index: number; }`  
`item-label`| `{ item: ContextMenuItem; active?: boolean | undefined; index: number; }`  
`item-trailing`| `{ item: ContextMenuItem; active?: boolean | undefined; index: number; }`  
`content-top`| `{}`  
`content-bottom`| `{}`  
  
### Emits

Event |  Type   
---|---  
`update:open`| `[payload: boolean]`  
  
## Theme

app.config.ts

    
    
    export default defineAppConfig({
      ui: {
        contextMenu: {
          slots: {
            content: 'min-w-32 bg-default shadow-lg rounded-md ring ring-default divide-y divide-default overflow-y-auto scroll-py-1 data-[state=open]:animate-[scale-in_100ms_ease-out] data-[state=closed]:animate-[scale-out_100ms_ease-in] origin-(--reka-context-menu-content-transform-origin)',
            group: 'p-1 isolate',
            label: 'w-full flex items-center font-semibold text-highlighted',
            separator: '-mx-1 my-1 h-px bg-border',
            item: 'group relative w-full flex items-center select-none outline-none before:absolute before:z-[-1] before:inset-px before:rounded-md data-disabled:cursor-not-allowed data-disabled:opacity-75',
            itemLeadingIcon: 'shrink-0',
            itemLeadingAvatar: 'shrink-0',
            itemLeadingAvatarSize: '',
            itemTrailing: 'ms-auto inline-flex gap-1.5 items-center',
            itemTrailingIcon: 'shrink-0',
            itemTrailingKbds: 'hidden lg:inline-flex items-center shrink-0',
            itemTrailingKbdsSize: '',
            itemLabel: 'truncate',
            itemLabelExternalIcon: 'inline-block size-3 align-top text-dimmed'
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
            active: {
              true: {
                item: 'text-highlighted before:bg-elevated',
                itemLeadingIcon: 'text-default'
              },
              false: {
                item: [
                  'text-default data-highlighted:text-highlighted data-[state=open]:text-highlighted data-highlighted:before:bg-elevated/50 data-[state=open]:before:bg-elevated/50',
                  'transition-colors before:transition-colors'
                ],
                itemLeadingIcon: [
                  'text-dimmed group-data-highlighted:text-default group-data-[state=open]:text-default',
                  'transition-colors'
                ]
              }
            },
            loading: {
              true: {
                itemLeadingIcon: 'animate-spin'
              }
            },
            size: {
              xs: {
                label: 'p-1 text-xs gap-1',
                item: 'p-1 text-xs gap-1',
                itemLeadingIcon: 'size-4',
                itemLeadingAvatarSize: '3xs',
                itemTrailingIcon: 'size-4',
                itemTrailingKbds: 'gap-0.5',
                itemTrailingKbdsSize: 'sm'
              },
              sm: {
                label: 'p-1.5 text-xs gap-1.5',
                item: 'p-1.5 text-xs gap-1.5',
                itemLeadingIcon: 'size-4',
                itemLeadingAvatarSize: '3xs',
                itemTrailingIcon: 'size-4',
                itemTrailingKbds: 'gap-0.5',
                itemTrailingKbdsSize: 'sm'
              },
              md: {
                label: 'p-1.5 text-sm gap-1.5',
                item: 'p-1.5 text-sm gap-1.5',
                itemLeadingIcon: 'size-5',
                itemLeadingAvatarSize: '2xs',
                itemTrailingIcon: 'size-5',
                itemTrailingKbds: 'gap-0.5',
                itemTrailingKbdsSize: 'md'
              },
              lg: {
                label: 'p-2 text-sm gap-2',
                item: 'p-2 text-sm gap-2',
                itemLeadingIcon: 'size-5',
                itemLeadingAvatarSize: '2xs',
                itemTrailingIcon: 'size-5',
                itemTrailingKbds: 'gap-1',
                itemTrailingKbdsSize: 'md'
              },
              xl: {
                label: 'p-2 text-base gap-2',
                item: 'p-2 text-base gap-2',
                itemLeadingIcon: 'size-6',
                itemLeadingAvatarSize: 'xs',
                itemTrailingIcon: 'size-6',
                itemTrailingKbds: 'gap-1',
                itemTrailingKbdsSize: 'lg'
              }
            }
          },
          compoundVariants: [
            {
              color: 'primary',
              active: false,
              class: {
                item: 'text-primary data-highlighted:text-primary data-highlighted:before:bg-primary/10 data-[state=open]:before:bg-primary/10',
                itemLeadingIcon: 'text-primary/75 group-data-highlighted:text-primary group-data-[state=open]:text-primary'
              }
            },
            {
              color: 'primary',
              active: true,
              class: {
                item: 'text-primary before:bg-primary/10',
                itemLeadingIcon: 'text-primary'
              }
            }
          ],
          defaultVariants: {
            size: 'md'
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
          ui: {
            contextMenu: {
              slots: {
                content: 'min-w-32 bg-default shadow-lg rounded-md ring ring-default divide-y divide-default overflow-y-auto scroll-py-1 data-[state=open]:animate-[scale-in_100ms_ease-out] data-[state=closed]:animate-[scale-out_100ms_ease-in] origin-(--reka-context-menu-content-transform-origin)',
                group: 'p-1 isolate',
                label: 'w-full flex items-center font-semibold text-highlighted',
                separator: '-mx-1 my-1 h-px bg-border',
                item: 'group relative w-full flex items-center select-none outline-none before:absolute before:z-[-1] before:inset-px before:rounded-md data-disabled:cursor-not-allowed data-disabled:opacity-75',
                itemLeadingIcon: 'shrink-0',
                itemLeadingAvatar: 'shrink-0',
                itemLeadingAvatarSize: '',
                itemTrailing: 'ms-auto inline-flex gap-1.5 items-center',
                itemTrailingIcon: 'shrink-0',
                itemTrailingKbds: 'hidden lg:inline-flex items-center shrink-0',
                itemTrailingKbdsSize: '',
                itemLabel: 'truncate',
                itemLabelExternalIcon: 'inline-block size-3 align-top text-dimmed'
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
                active: {
                  true: {
                    item: 'text-highlighted before:bg-elevated',
                    itemLeadingIcon: 'text-default'
                  },
                  false: {
                    item: [
                      'text-default data-highlighted:text-highlighted data-[state=open]:text-highlighted data-highlighted:before:bg-elevated/50 data-[state=open]:before:bg-elevated/50',
                      'transition-colors before:transition-colors'
                    ],
                    itemLeadingIcon: [
                      'text-dimmed group-data-highlighted:text-default group-data-[state=open]:text-default',
                      'transition-colors'
                    ]
                  }
                },
                loading: {
                  true: {
                    itemLeadingIcon: 'animate-spin'
                  }
                },
                size: {
                  xs: {
                    label: 'p-1 text-xs gap-1',
                    item: 'p-1 text-xs gap-1',
                    itemLeadingIcon: 'size-4',
                    itemLeadingAvatarSize: '3xs',
                    itemTrailingIcon: 'size-4',
                    itemTrailingKbds: 'gap-0.5',
                    itemTrailingKbdsSize: 'sm'
                  },
                  sm: {
                    label: 'p-1.5 text-xs gap-1.5',
                    item: 'p-1.5 text-xs gap-1.5',
                    itemLeadingIcon: 'size-4',
                    itemLeadingAvatarSize: '3xs',
                    itemTrailingIcon: 'size-4',
                    itemTrailingKbds: 'gap-0.5',
                    itemTrailingKbdsSize: 'sm'
                  },
                  md: {
                    label: 'p-1.5 text-sm gap-1.5',
                    item: 'p-1.5 text-sm gap-1.5',
                    itemLeadingIcon: 'size-5',
                    itemLeadingAvatarSize: '2xs',
                    itemTrailingIcon: 'size-5',
                    itemTrailingKbds: 'gap-0.5',
                    itemTrailingKbdsSize: 'md'
                  },
                  lg: {
                    label: 'p-2 text-sm gap-2',
                    item: 'p-2 text-sm gap-2',
                    itemLeadingIcon: 'size-5',
                    itemLeadingAvatarSize: '2xs',
                    itemTrailingIcon: 'size-5',
                    itemTrailingKbds: 'gap-1',
                    itemTrailingKbdsSize: 'md'
                  },
                  xl: {
                    label: 'p-2 text-base gap-2',
                    item: 'p-2 text-base gap-2',
                    itemLeadingIcon: 'size-6',
                    itemLeadingAvatarSize: 'xs',
                    itemTrailingIcon: 'size-6',
                    itemTrailingKbds: 'gap-1',
                    itemTrailingKbdsSize: 'lg'
                  }
                }
              },
              compoundVariants: [
                {
                  color: 'primary',
                  active: false,
                  class: {
                    item: 'text-primary data-highlighted:text-primary data-highlighted:before:bg-primary/10 data-[state=open]:before:bg-primary/10',
                    itemLeadingIcon: 'text-primary/75 group-data-highlighted:text-primary group-data-[state=open]:text-primary'
                  }
                },
                {
                  color: 'primary',
                  active: true,
                  class: {
                    item: 'text-primary before:bg-primary/10',
                    itemLeadingIcon: 'text-primary'
                  }
                }
              ],
              defaultVariants: {
                size: 'md'
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
          ui: {
            contextMenu: {
              slots: {
                content: 'min-w-32 bg-default shadow-lg rounded-md ring ring-default divide-y divide-default overflow-y-auto scroll-py-1 data-[state=open]:animate-[scale-in_100ms_ease-out] data-[state=closed]:animate-[scale-out_100ms_ease-in] origin-(--reka-context-menu-content-transform-origin)',
                group: 'p-1 isolate',
                label: 'w-full flex items-center font-semibold text-highlighted',
                separator: '-mx-1 my-1 h-px bg-border',
                item: 'group relative w-full flex items-center select-none outline-none before:absolute before:z-[-1] before:inset-px before:rounded-md data-disabled:cursor-not-allowed data-disabled:opacity-75',
                itemLeadingIcon: 'shrink-0',
                itemLeadingAvatar: 'shrink-0',
                itemLeadingAvatarSize: '',
                itemTrailing: 'ms-auto inline-flex gap-1.5 items-center',
                itemTrailingIcon: 'shrink-0',
                itemTrailingKbds: 'hidden lg:inline-flex items-center shrink-0',
                itemTrailingKbdsSize: '',
                itemLabel: 'truncate',
                itemLabelExternalIcon: 'inline-block size-3 align-top text-dimmed'
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
                active: {
                  true: {
                    item: 'text-highlighted before:bg-elevated',
                    itemLeadingIcon: 'text-default'
                  },
                  false: {
                    item: [
                      'text-default data-highlighted:text-highlighted data-[state=open]:text-highlighted data-highlighted:before:bg-elevated/50 data-[state=open]:before:bg-elevated/50',
                      'transition-colors before:transition-colors'
                    ],
                    itemLeadingIcon: [
                      'text-dimmed group-data-highlighted:text-default group-data-[state=open]:text-default',
                      'transition-colors'
                    ]
                  }
                },
                loading: {
                  true: {
                    itemLeadingIcon: 'animate-spin'
                  }
                },
                size: {
                  xs: {
                    label: 'p-1 text-xs gap-1',
                    item: 'p-1 text-xs gap-1',
                    itemLeadingIcon: 'size-4',
                    itemLeadingAvatarSize: '3xs',
                    itemTrailingIcon: 'size-4',
                    itemTrailingKbds: 'gap-0.5',
                    itemTrailingKbdsSize: 'sm'
                  },
                  sm: {
                    label: 'p-1.5 text-xs gap-1.5',
                    item: 'p-1.5 text-xs gap-1.5',
                    itemLeadingIcon: 'size-4',
                    itemLeadingAvatarSize: '3xs',
                    itemTrailingIcon: 'size-4',
                    itemTrailingKbds: 'gap-0.5',
                    itemTrailingKbdsSize: 'sm'
                  },
                  md: {
                    label: 'p-1.5 text-sm gap-1.5',
                    item: 'p-1.5 text-sm gap-1.5',
                    itemLeadingIcon: 'size-5',
                    itemLeadingAvatarSize: '2xs',
                    itemTrailingIcon: 'size-5',
                    itemTrailingKbds: 'gap-0.5',
                    itemTrailingKbdsSize: 'md'
                  },
                  lg: {
                    label: 'p-2 text-sm gap-2',
                    item: 'p-2 text-sm gap-2',
                    itemLeadingIcon: 'size-5',
                    itemLeadingAvatarSize: '2xs',
                    itemTrailingIcon: 'size-5',
                    itemTrailingKbds: 'gap-1',
                    itemTrailingKbdsSize: 'md'
                  },
                  xl: {
                    label: 'p-2 text-base gap-2',
                    item: 'p-2 text-base gap-2',
                    itemLeadingIcon: 'size-6',
                    itemLeadingAvatarSize: 'xs',
                    itemTrailingIcon: 'size-6',
                    itemTrailingKbds: 'gap-1',
                    itemTrailingKbdsSize: 'lg'
                  }
                }
              },
              compoundVariants: [
                {
                  color: 'primary',
                  active: false,
                  class: {
                    item: 'text-primary data-highlighted:text-primary data-highlighted:before:bg-primary/10 data-[state=open]:before:bg-primary/10',
                    itemLeadingIcon: 'text-primary/75 group-data-highlighted:text-primary group-data-[state=open]:text-primary'
                  }
                },
                {
                  color: 'primary',
                  active: true,
                  class: {
                    item: 'text-primary before:bg-primary/10',
                    itemLeadingIcon: 'text-primary'
                  }
                }
              ],
              defaultVariants: {
                size: 'md'
              }
            }
          }
        })
      ]
    })
    

Expand code

[](https://github.com/nuxt/ui/blob/v3/src/theme/context-menu.ts "Compound
variants")Some colors in `compoundVariants` are omitted for readability. Check
out the source code on GitHub.

[ContainerA container lets you center and constrain the width of your
content.](/components/container)[DrawerA drawer that smoothly slides in & out
of the screen.](/components/drawer)


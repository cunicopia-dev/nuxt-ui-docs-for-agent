<!-- source: https://ui.nuxt.com/components/dropdown-menu --> # DropdownMenu

[DropdownMenu](https://reka-ui.com/docs/components/dropdown-
menu)[GitHub](https://github.com/nuxt/ui/tree/v3/src/runtime/components/DropdownMenu.vue)

A menu to display actions when clicking on an element.

## Usage

Use a [Button](/components/button) or any other component in the default slot
of the DropdownMenu.

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
  * `children?: DropdownMenuItem[] | DropdownMenuItem[][]`

You can pass any property from the [Link](/components/link#props) component
such as `to`, `target`, etc.

    
    
    <script setup lang="ts">
    import type { DropdownMenuItem } from '@nuxt/ui'
    
    const items = ref<DropdownMenuItem[][]>([
      [
        {
          label: 'Benjamin',
          avatar: {
            src: 'https://github.com/benjamincanac.png'
          },
          type: 'label'
        }
      ],
      [
        {
          label: 'Profile',
          icon: 'i-lucide-user'
        },
        {
          label: 'Billing',
          icon: 'i-lucide-credit-card'
        },
        {
          label: 'Settings',
          icon: 'i-lucide-cog',
          kbds: [',']
        },
        {
          label: 'Keyboard shortcuts',
          icon: 'i-lucide-monitor'
        }
      ],
      [
        {
          label: 'Team',
          icon: 'i-lucide-users'
        },
        {
          label: 'Invite users',
          icon: 'i-lucide-user-plus',
          children: [
            [
              {
                label: 'Email',
                icon: 'i-lucide-mail'
              },
              {
                label: 'Message',
                icon: 'i-lucide-message-square'
              }
            ],
            [
              {
                label: 'More',
                icon: 'i-lucide-circle-plus'
              }
            ]
          ]
        },
        {
          label: 'New team',
          icon: 'i-lucide-plus',
          kbds: ['meta', 'n']
        }
      ],
      [
        {
          label: 'GitHub',
          icon: 'i-simple-icons-github',
          to: 'https://github.com/nuxt/ui',
          target: '_blank'
        },
        {
          label: 'Support',
          icon: 'i-lucide-life-buoy',
          to: '/components/dropdown-menu'
        },
        {
          label: 'API',
          icon: 'i-lucide-cloud',
          disabled: true
        }
      ],
      [
        {
          label: 'Logout',
          icon: 'i-lucide-log-out',
          kbds: ['shift', 'meta', 'q']
        }
      ]
    ])
    </script>
    
    <template>
      <UDropdownMenu
        :items="items"
        :ui="{
          content: 'w-48'
        }"
      >
        <UButton icon="i-lucide-menu" color="neutral" variant="outline" />
      </UDropdownMenu>
    </template>
    

Expand code

You can also pass an array of arrays to the `items` prop to create separated
groups of items.

Each item can take a `children` array of objects with the same properties as
the `items` prop to create a nested menu which can be controlled using the
`open`, `defaultOpen` and `content` properties.

### Content

Use the `content` prop to control how the DropdownMenu content is rendered,
like its `align` or `side` for example.

content.align

start

content.side

bottom

content.sideOffset

    
    
    <script setup lang="ts">
    import type { DropdownMenuItem } from '@nuxt/ui'
    
    const items = ref<DropdownMenuItem[]>([
      {
        label: 'Profile',
        icon: 'i-lucide-user'
      },
      {
        label: 'Billing',
        icon: 'i-lucide-credit-card'
      },
      {
        label: 'Settings',
        icon: 'i-lucide-cog'
      }
    ])
    </script>
    
    <template>
      <UDropdownMenu
        :items="items"
        :content="{
          align: 'start',
          side: 'bottom',
          sideOffset: 8
        }"
        :ui="{
          content: 'w-48'
        }"
      >
        <UButton label="Open" icon="i-lucide-menu" color="neutral" variant="outline" />
      </UDropdownMenu>
    </template>
    

### Arrow

Use the `arrow` prop to display an arrow on the DropdownMenu.

    
    
    <script setup lang="ts">
    import type { DropdownMenuItem } from '@nuxt/ui'
    
    const items = ref<DropdownMenuItem[]>([
      {
        label: 'Profile',
        icon: 'i-lucide-user'
      },
      {
        label: 'Billing',
        icon: 'i-lucide-credit-card'
      },
      {
        label: 'Settings',
        icon: 'i-lucide-cog'
      }
    ])
    </script>
    
    <template>
      <UDropdownMenu
        arrow
        :items="items"
        :ui="{
          content: 'w-48'
        }"
      >
        <UButton label="Open" icon="i-lucide-menu" color="neutral" variant="outline" />
      </UDropdownMenu>
    </template>
    

### Size

Use the `size` prop to control the size of the DropdownMenu.

size

xl

    
    
    <script setup lang="ts">
    import type { DropdownMenuItem } from '@nuxt/ui'
    
    const items = ref<DropdownMenuItem[]>([
      {
        label: 'Profile',
        icon: 'i-lucide-user'
      },
      {
        label: 'Billing',
        icon: 'i-lucide-credit-card'
      },
      {
        label: 'Settings',
        icon: 'i-lucide-cog'
      }
    ])
    </script>
    
    <template>
      <UDropdownMenu
        size="xl"
        :items="items"
        :content="{
          align: 'start'
        }"
        :ui="{
          content: 'w-48'
        }"
      >
        <UButton size="xl" label="Open" icon="i-lucide-menu" color="neutral" variant="outline" />
      </UDropdownMenu>
    </template>
    

The `size` prop will not be proxied to the Button, you need to set it
yourself.

When using the same size, the DropdownMenu items will be perfectly aligned
with the Button.

### Disabled

Use the `disabled` prop to disable the DropdownMenu.

disabled

true

    
    
    <script setup lang="ts">
    import type { DropdownMenuItem } from '@nuxt/ui'
    
    const items = ref<DropdownMenuItem[]>([
      {
        label: 'Profile',
        icon: 'i-lucide-user'
      },
      {
        label: 'Billing',
        icon: 'i-lucide-credit-card'
      },
      {
        label: 'Settings',
        icon: 'i-lucide-cog'
      }
    ])
    </script>
    
    <template>
      <UDropdownMenu
        disabled
        :items="items"
        :ui="{
          content: 'w-48'
        }"
      >
        <UButton label="Open" icon="i-lucide-menu" color="neutral" variant="outline" />
      </UDropdownMenu>
    </template>
    

## Examples

### With checkbox items

You can use the `type` property with `checkbox` and use the `checked` /
`onUpdateChecked` properties to control the checked state of the item.

Open

    
    
    <script setup lang="ts">
    import type { DropdownMenuItem } from '@nuxt/ui'
    
    const showBookmarks = ref(true)
    const showHistory = ref(false)
    const showDownloads = ref(false)
    
    const items = computed(() => [{
      label: 'Interface',
      icon: 'i-lucide-app-window',
      type: 'label' as const
    }, {
      type: 'separator' as const
    }, {
      label: 'Show Bookmarks',
      icon: 'i-lucide-bookmark',
      type: 'checkbox' as const,
      checked: showBookmarks.value,
      onUpdateChecked(checked: boolean) {
        showBookmarks.value = checked
      },
      onSelect(e: Event) {
        e.preventDefault()
      }
    }, {
      label: 'Show History',
      icon: 'i-lucide-clock',
      type: 'checkbox' as const,
      checked: showHistory.value,
      onUpdateChecked(checked: boolean) {
        showHistory.value = checked
      }
    }, {
      label: 'Show Downloads',
      icon: 'i-lucide-download',
      type: 'checkbox' as const,
      checked: showDownloads.value,
      onUpdateChecked(checked: boolean) {
        showDownloads.value = checked
      }
    }] satisfies DropdownMenuItem[])
    </script>
    
    <template>
      <UDropdownMenu :items="items" :content="{ align: 'start' }" :ui="{ content: 'w-48' }">
        <UButton label="Open" color="neutral" variant="outline" icon="i-lucide-menu" />
      </UDropdownMenu>
    </template>
    

Expand code

To ensure reactivity for the `checked` state of items, it's recommended to
wrap your `items` array inside a `computed`.

### With color items

You can use the `color` property to highlight certain items with a color.

Open

    
    
    <script setup lang="ts">
    import type { DropdownMenuItem } from '@nuxt/ui'
    
    const items: DropdownMenuItem[][] = [
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
          color: 'error',
          icon: 'i-lucide-trash'
        }
      ]
    ]
    </script>
    
    <template>
      <UDropdownMenu :items="items" :ui="{ content: 'w-48' }">
        <UButton label="Open" color="neutral" variant="outline" icon="i-lucide-menu" />
      </UDropdownMenu>
    </template>
    

### Control open state

You can control the open state by using the `default-open` prop or the
`v-model:open` directive.

Open

    
    
    <script setup lang="ts">
    import type { DropdownMenuItem } from '@nuxt/ui'
    
    const open = ref(false)
    
    defineShortcuts({
      o: () => open.value = !open.value
    })
    
    const items: DropdownMenuItem[] = [
      {
        label: 'Profile',
        icon: 'i-lucide-user'
      }, {
        label: 'Billing',
        icon: 'i-lucide-credit-card'
      }, {
        label: 'Settings',
        icon: 'i-lucide-cog'
      }
    ]
    </script>
    
    <template>
      <UDropdownMenu v-model:open="open" :items="items" :ui="{ content: 'w-48' }">
        <UButton label="Open" color="neutral" variant="outline" icon="i-lucide-menu" />
      </UDropdownMenu>
    </template>
    

In this example, leveraging [`defineShortcuts`](/composables/define-
shortcuts), you can toggle the DropdownMenu by pressing `O`.

### With custom slot

Use the `slot` property to customize a specific item.

You will have access to the following slots:

  * `#{{ item.slot }}`
  * `#{{ item.slot }}-leading`
  * `#{{ item.slot }}-label`
  * `#{{ item.slot }}-trailing`

Open

    
    
    <script setup lang="ts">
    import type { DropdownMenuItem } from '@nuxt/ui'
    
    const items = [
      {
        label: 'Profile',
        icon: 'i-lucide-user',
        slot: 'profile' as const
      }, {
        label: 'Billing',
        icon: 'i-lucide-credit-card'
      }, {
        label: 'Settings',
        icon: 'i-lucide-cog'
      }
    ] satisfies DropdownMenuItem[]
    </script>
    
    <template>
      <UDropdownMenu :items="items" :ui="{ content: 'w-48' }">
        <UButton label="Open" color="neutral" variant="outline" icon="i-lucide-menu" />
    
        <template #profile-trailing>
          <UIcon name="i-lucide-badge-check" class="shrink-0 size-5 text-primary" />
        </template>
      </UDropdownMenu>
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
    import type { DropdownMenuItem } from '@nuxt/ui'
    
    const items: DropdownMenuItem[] = [{
      label: 'Invite users',
      icon: 'i-lucide-user-plus',
      children: [{
        label: 'Invite by email',
        icon: 'i-lucide-send-horizontal',
        kbds: ['meta', 'e'],
        onSelect() {
          console.log('Invite by email clicked')
        }
      }, {
        label: 'Invite by link',
        icon: 'i-lucide-link',
        kbds: ['meta', 'i'],
        onSelect() {
          console.log('Invite by link clicked')
        }
      }]
    }, {
      label: 'New team',
      icon: 'i-lucide-plus',
      kbds: ['meta', 'n'],
      onSelect() {
        console.log('New team clicked')
      }
    }]
    
    defineShortcuts(extractShortcuts(items))
    </script>
    

In this example, ` ``E`, ` ``I` and ` ``N` would trigger the `select` function
of the corresponding item.

## API

### Props

Prop |  Default |  Type   
---|---|---  
`size`| `'md'`| ` "sm" | "md" | "xs" | "lg" | "xl"`  
`items`| | ` DropdownMenuItem[] | DropdownMenuItem[][]`Show properties

  * `label?: string`
  * `icon?: string`
  * `color?: "error" | "primary" | "secondary" | "success" | "info" | "warning" | "neutral"`
  * `avatar?: AvatarProps`
  * `content?: (DropdownMenuContentProps & Partial<EmitsToProps<MenuContentEmits>>)`
  * `kbds?: (string )[] | KbdProps[] | undefined`
  * `type?: "label" | "separator" | "link" | "checkbox"`The item type. Defaults to `'link'`.
  * `slot?: string`
  * `loading?: boolean`
  * `disabled?: boolean`
  * `checked?: boolean`
  * `open?: boolean`
  * `defaultOpen?: boolean`
  * `children?: ArrayOrNested<DropdownMenuItem>`
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
`content`| `{ side: 'bottom', sideOffset: 8, collisionPadding: 8 }`| `
DropdownMenuContentProps & Partial<EmitsToProps<MenuContentEmits>>`The content
of the menu.Show properties

  * `side?: "top" | "right" | "bottom" | "left"`The preferred side of the trigger to render against when open. Will be reversed when collisions occur and avoidCollisions is enabled. Defaults to `"top"`.
  * `sideOffset?: number`The distance in pixels from the trigger. Defaults to `0`.
  * `align?: "end" | "start" | "center"`The preferred alignment against the trigger. May change when collisions occur. Defaults to `"center"`.
  * `alignOffset?: number`An offset in pixels from the `start` or `end` alignment options. Defaults to `0`.
  * `avoidCollisions?: boolean`When `true`, overrides the side and align preferences to prevent collisions with boundary edges. Defaults to `true`.
  * `collisionBoundary?: Element | (Element | null)[] | null`The element used as the collision boundary. By default this is the viewport, though you can provide additional element(s) to be included in this check. Defaults to `[]`.
  * `collisionPadding?: number | Partial<Record<"top" | "right" | "bottom" | "left", number>>`The distance in pixels from the boundary edges where collision detection should occur. Accepts a number (same for all sides), or a partial padding object, for example: { top: 20, left: 20 }. Defaults to `0`.
  * `arrowPadding?: number`The padding between the arrow and the edges of the content. If your content has border-radius, this will prevent it from overflowing the corners. Defaults to `0`.
  * `sticky?: "partial" | "always"`The sticky behavior on the align axis. `partial` will keep the content in the boundary as long as the trigger is at least partially in the boundary whilst "always" will keep the content in the boundary regardless. Defaults to `"partial"`.
  * `hideWhenDetached?: boolean`Whether to hide the content when the trigger becomes fully occluded. Defaults to `false`.
  * `positionStrategy?: "fixed" | "absolute"`The type of CSS position property to use.
  * `updatePositionStrategy?: "always" | "optimized"`Strategy to update the position of the floating element on every animation frame. Defaults to `'optimized'`.
  * `disableUpdateOnLayoutShift?: boolean`Whether to disable the update position for the content when the layout shifted. Defaults to `false`.
  * `prioritizePosition?: boolean`Force content to be position within the viewport.Might overlap the reference element, which may not be desired. Defaults to `false`.
  * `reference?: ReferenceElement`The custom element or virtual element that will be set as the reference to position the floating element.If provided, it will replace the default anchor element.
  * `loop?: boolean`When `true`, keyboard navigation will loop from last item to first, and vice versa. Defaults to `false`.
  * `onEscapeKeyDown?: ((event: KeyboardEvent) => void)`
  * `onPointerDownOutside?: ((event: PointerDownOutsideEvent) => void)`
  * `onFocusOutside?: ((event: FocusOutsideEvent) => void)`
  * `onInteractOutside?: ((event: PointerDownOutsideEvent | FocusOutsideEvent) => void)`
  * `onCloseAutoFocus?: ((event: Event) => void)`

  
`arrow`| `false`| `boolean | DropdownMenuArrowProps`Display an arrow alongside the menu.  
`portal`| `true`| ` string | false | true | HTMLElement`Render the menu in a portal.  
`labelKey`| `'label'`| ` string | number`The key used to get the label from the item.  
`disabled`| | `boolean`  
`defaultOpen`| | `boolean`The open state of the dropdown menu when it is initially rendered. Use when you do not need to control its open state.  
`open`| | `boolean`The controlled open state of the menu. Can be used as `v-model:open`.  
`modal`| `true`| `boolean`The modality of the dropdown menu.When set to
`true`, interaction with outside elements will be disabled and only menu
content will be visible to screen readers.  
`ui`| | ` { content?: ClassNameValue; arrow?: ClassNameValue; group?: ClassNameValue; label?: ClassNameValue; separator?: ClassNameValue; ... 9 more ...; itemLabelExternalIcon?: ClassNameValue; }`  
  
### Slots

Slot |  Type   
---|---  
`default`| `{ open: boolean; }`  
`item`| `{ item: DropdownMenuItem; active?: boolean | undefined; index: number; }`  
`item-leading`| `{ item: DropdownMenuItem; active?: boolean | undefined; index: number; }`  
`item-label`| `{ item: DropdownMenuItem; active?: boolean | undefined; index: number; }`  
`item-trailing`| `{ item: DropdownMenuItem; active?: boolean | undefined; index: number; }`  
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
        dropdownMenu: {
          slots: {
            content: 'min-w-32 bg-default shadow-lg rounded-md ring ring-default divide-y divide-default overflow-y-auto scroll-py-1 data-[state=open]:animate-[scale-in_100ms_ease-out] data-[state=closed]:animate-[scale-out_100ms_ease-in] origin-(--reka-dropdown-menu-content-transform-origin)',
            arrow: 'fill-default',
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
            dropdownMenu: {
              slots: {
                content: 'min-w-32 bg-default shadow-lg rounded-md ring ring-default divide-y divide-default overflow-y-auto scroll-py-1 data-[state=open]:animate-[scale-in_100ms_ease-out] data-[state=closed]:animate-[scale-out_100ms_ease-in] origin-(--reka-dropdown-menu-content-transform-origin)',
                arrow: 'fill-default',
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
            dropdownMenu: {
              slots: {
                content: 'min-w-32 bg-default shadow-lg rounded-md ring ring-default divide-y divide-default overflow-y-auto scroll-py-1 data-[state=open]:animate-[scale-in_100ms_ease-out] data-[state=closed]:animate-[scale-out_100ms_ease-in] origin-(--reka-dropdown-menu-content-transform-origin)',
                arrow: 'fill-default',
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

[](https://github.com/nuxt/ui/blob/v3/src/theme/dropdown-menu.ts "Compound
variants")Some colors in `compoundVariants` are omitted for readability. Check
out the source code on GitHub.

[DrawerA drawer that smoothly slides in & out of the
screen.](/components/drawer)[FormA form component with built-in validation and
submission handling.](/components/form)


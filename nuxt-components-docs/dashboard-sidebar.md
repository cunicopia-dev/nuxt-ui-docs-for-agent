<!-- source: https://ui.nuxt.com/components/dashboard-sidebar --> # DashboardSidebarPRO

[GitHub](https://github.com/nuxt/ui-
pro/tree/v3/src/runtime/components/DashboardSidebar.vue)

A resizable and collapsible sidebar to display in a dashboard.

## Usage

The DashboardSidebar component is used to display a sidebar. Its state (size,
collapsed, etc.) will be saved based on the `storage` and `storage-key` props
you provide to the [DashboardGroup](/components/dashboard-group#props)
component.

Use it inside the default slot of the [DashboardGroup](/components/dashboard-
group) component:

layouts/dashboard.vue

    
    
    <template>
      <UDashboardGroup>
        <UDashboardSidebar />
    
        <slot />
      </UDashboardGroup>
    </template>
    

Use the `left`, `default` and `right` slots to customize the sidebar and the
`body` or `content` slots to customize the sidebar menu.

Search...

` ``K`

![](https://github.com/benjamincanac.png)Benjamin

    
    
    <script setup lang="ts">
    import type { NavigationMenuItem } from '@nuxt/ui'
    
    const items: NavigationMenuItem[][] = [[{
      label: 'Home',
      icon: 'i-lucide-house',
      active: true
    }, {
      label: 'Inbox',
      icon: 'i-lucide-inbox',
      badge: '4'
    }, {
      label: 'Contacts',
      icon: 'i-lucide-users'
    }, {
      label: 'Settings',
      icon: 'i-lucide-settings',
      defaultOpen: true,
      children: [{
        label: 'General'
      }, {
        label: 'Members'
      }, {
        label: 'Notifications'
      }]
    }], [{
      label: 'Feedback',
      icon: 'i-lucide-message-circle',
      to: 'https://github.com/nuxt-ui-pro/dashboard',
      target: '_blank'
    }, {
      label: 'Help & Support',
      icon: 'i-lucide-info',
      to: 'https://github.com/nuxt/ui-pro',
      target: '_blank'
    }]]
    </script>
    
    <template>
      <UDashboardSidebar collapsible resizable :ui="{ footer: 'border-t border-default' }">
        <template #header="{ collapsed }">
          <LogoPro :collapsed="collapsed" class="h-5 w-auto shrink-0" />
        </template>
    
        <template #default="{ collapsed }">
          <UButton
            :label="collapsed ? undefined : 'Search...'"
            icon="i-lucide-search"
            color="neutral"
            variant="outline"
            block
            :square="collapsed"
          >
            <template v-if="!collapsed" #trailing>
              <div class="flex items-center gap-0.5 ms-auto">
                <UKbd value="meta" variant="subtle" />
                <UKbd value="K" variant="subtle" />
              </div>
            </template>
          </UButton>
    
          <UNavigationMenu
            :collapsed="collapsed"
            :items="items[0]"
            orientation="vertical"
          />
    
          <UNavigationMenu
            :collapsed="collapsed"
            :items="items[1]"
            orientation="vertical"
            class="mt-auto"
          />
        </template>
    
        <template #footer="{ collapsed }">
          <UButton
            :avatar="{
              src: 'https://github.com/benjamincanac.png'
            }"
            :label="collapsed ? undefined : 'Benjamin'"
            color="neutral"
            variant="ghost"
            class="w-full"
            :block="collapsed"
          />
        </template>
      </UDashboardSidebar>
    </template>
    

Expand code

Drag the sidebar near the left edge of the screen to collapse it.

### Resizable

Use the `resizable` prop to make the sidebar resizable.

resizable

true

    
    
    <template>
      <UDashboardSidebar resizable>
        <Placeholder class="h-96" />
      </UDashboardSidebar>
    </template>
    

### Collapsible

Use the `collapsible` prop to make the sidebar collapsible when dragging near
the edge of the screen.

The [`DashboardSidebarCollapse`](/components/dashboard-sidebar-collapse)
component will have no effect if the sidebar is not **collapsible**.

collapsible

true

    
    
    <template>
      <UDashboardSidebar resizable collapsible>
        <Placeholder class="h-96" />
      </UDashboardSidebar>
    </template>
    

You can access the `collapsed` state in the slot props to customize the
content of the sidebar when it is collapsed.

### Size

Use the `min-size`, `max-size`, `default-size` and `collapsed-size` props to
customize the size of the sidebar.

minSize

defaultSize

maxSize

collapsedSize

    
    
    <template>
      <UDashboardSidebar
        resizable
        collapsible
        :min-size="22"
        :default-size="35"
        :max-size="40"
        :collapsed-size="0"
      >
        <Placeholder class="h-96" />
      </UDashboardSidebar>
    </template>
    

The `collapsed-size` prop is set to `0` by default but the sidebar has a
`min-w-16` to make sure it is visible.

### Side

Use the `side` prop to change the side of the sidebar. Defaults to `left`.

side

right

    
    
    <template>
      <UDashboardSidebar side="right" resizable collapsible>
        <Placeholder class="h-96" />
      </UDashboardSidebar>
    </template>
    

### Mode

Use the `mode` prop to change the mode of the sidebar menu. Defaults to
`slideover`.

Use the `body` slot to fill the menu body (under the header) or the `content`
slot to fill the entire menu.

You can use the `menu` prop to customize the menu of the sidebar, it will
adapt depending on the mode you choose.

mode

drawer

    
    
    <script setup lang="ts">
    import type { NavigationMenuItem } from '@nuxt/ui'
    
    defineProps<{
      mode: 'drawer' | 'slideover' | 'modal'
    }>()
    
    const items: NavigationMenuItem[] = [{
      label: 'Home',
      icon: 'i-lucide-house',
      active: true
    }, {
      label: 'Inbox',
      icon: 'i-lucide-inbox'
    }, {
      label: 'Contacts',
      icon: 'i-lucide-users'
    }]
    </script>
    
    <template>
      <UDashboardGroup>
        <UDashboardSidebar :mode="mode">
          <template #header>
            <LogoPro class="h-5 w-auto" />
          </template>
    
          <UNavigationMenu
            :items="items"
            orientation="vertical"
          />
        </UDashboardSidebar>
    
        <UDashboardPanel>
          <template #header>
            <UDashboardNavbar title="Dashboard" />
          </template>
        </UDashboardPanel>
      </UDashboardGroup>
    </template>
    

Expand code

These examples contain the [`DashboardGroup`](/components/dashboard-group),
[`DashboardPanel`](/components/dashboard-panel) and
[`DashboardNavbar`](/components/dashboard-navbar) components as they are
required to demonstrate the sidebar on mobile.

### Toggle

Use the `toggle` prop to customize the
[DashboardSidebarToggle](/components/dashboard-sidebar-toggle) component
displayed on mobile.

You can pass any property from the [Button](/components/button) component to
customize it.

    
    
    <script setup lang="ts">
    import type { NavigationMenuItem } from '@nuxt/ui'
    
    const items: NavigationMenuItem[] = [{
      label: 'Home',
      icon: 'i-lucide-house',
      active: true
    }, {
      label: 'Inbox',
      icon: 'i-lucide-inbox'
    }, {
      label: 'Contacts',
      icon: 'i-lucide-users'
    }]
    </script>
    
    <template>
      <UDashboardGroup>
        <UDashboardSidebar
          open
          :toggle="{
            color: 'primary',
            variant: 'subtle',
            class: 'rounded-full'
          }"
        >
          <template #header>
            <LogoPro class="h-5 w-auto" />
          </template>
    
          <UNavigationMenu
            :items="items"
            orientation="vertical"
          />
        </UDashboardSidebar>
    
        <UDashboardPanel>
          <template #header>
            <UDashboardNavbar title="Dashboard" />
          </template>
        </UDashboardPanel>
      </UDashboardGroup>
    </template>
    

Expand code

### Toggle Side

Use the `toggle-side` prop to change the side of the toggle button. Defaults
to `left`.

    
    
    <script setup lang="ts">
    import type { NavigationMenuItem } from '@nuxt/ui'
    
    const items: NavigationMenuItem[] = [{
      label: 'Home',
      icon: 'i-lucide-house',
      active: true
    }, {
      label: 'Inbox',
      icon: 'i-lucide-inbox'
    }, {
      label: 'Contacts',
      icon: 'i-lucide-users'
    }]
    </script>
    
    <template>
      <UDashboardGroup>
        <UDashboardSidebar
          open
          toggle-side="right"
        >
          <template #header>
            <LogoPro class="h-5 w-auto" />
          </template>
    
          <UNavigationMenu
            :items="items"
            orientation="vertical"
          />
        </UDashboardSidebar>
    
        <UDashboardPanel>
          <template #header>
            <UDashboardNavbar title="Dashboard" />
          </template>
        </UDashboardPanel>
      </UDashboardGroup>
    </template>
    

Expand code

## Examples

### Control open state

You can control the open state by using the `open` prop or the `v-model:open`
directive.

    
    
    <script setup lang="ts">
    import type { NavigationMenuItem } from '@nuxt/ui'
    
    const items: NavigationMenuItem[] = [{
      label: 'Home',
      icon: 'i-lucide-house',
      active: true
    }, {
      label: 'Inbox',
      icon: 'i-lucide-inbox'
    }, {
      label: 'Contacts',
      icon: 'i-lucide-users'
    }]
    
    const open = ref(true)
    
    defineShortcuts({
      o: () => open.value = !open.value
    })
    </script>
    
    <template>
      <UDashboardSidebar v-model:open="open">
        <template #header>
          <LogoPro class="h-5 w-auto" />
        </template>
    
        <UNavigationMenu
          :items="items"
          orientation="vertical"
        />
      </UDashboardSidebar>
    </template>
    

In this example, leveraging [`defineShortcuts`](/composables/define-
shortcuts), you can toggle the open state of the DashboardSidebar by pressing
`O`.

### Control collapsed state

You can control the collapsed state by using the `collapsed` prop or the
`v-model:collapsed` directive.

    
    
    <script setup lang="ts">
    import type { NavigationMenuItem } from '@nuxt/ui'
    
    const items: NavigationMenuItem[] = [{
      label: 'Home',
      icon: 'i-lucide-house',
      active: true
    }, {
      label: 'Inbox',
      icon: 'i-lucide-inbox'
    }, {
      label: 'Contacts',
      icon: 'i-lucide-users'
    }]
    
    const collapsed = ref(false)
    
    defineShortcuts({
      c: () => collapsed.value = !collapsed.value
    })
    </script>
    
    <template>
      <UDashboardSidebar v-model:collapsed="collapsed" collapsible>
        <template #header>
          <LogoPro class="h-5 w-auto" :collapsed="collapsed" />
        </template>
    
        <UNavigationMenu
          :collapsed="collapsed"
          :items="items"
          orientation="vertical"
        />
      </UDashboardSidebar>
    </template>
    

In this example, leveraging [`defineShortcuts`](/composables/define-
shortcuts), you can toggle the collapsed state of the DashboardSidebar by
pressing `C`.

## API

### Props

Prop |  Default |  Type   
---|---|---  
`open`| | `boolean`  
`collapsed`| | `boolean`  
`mode`| `'slideover'`| ` "modal" | "slideover" | "drawer"`The mode of the sidebar menu.  
`menu`| | ` ModalProps | SlideoverProps | DrawerProps`The props for the sidebar menu component.Show properties

  * `title?: string`
  * `description?: string`
  * `content?: (DialogContentProps & Partial<EmitsToProps<DialogContentImplEmits>>)`The content of the modal.
  * `overlay?: boolean`Render an overlay behind the modal. Defaults to `true`.
  * `transition?: boolean`Animate the modal when opening or closing. Defaults to `true`.
  * `fullscreen?: boolean`When `true`, the modal will take up the full screen. Defaults to `false`.
  * `portal?: string | boolean | HTMLElement`Render the modal in a portal. Defaults to `true`.
  * `close?: boolean | Partial<ButtonProps>`Display a close button to dismiss the modal. `{ size: 'md', color: 'neutral', variant: 'ghost' }` Defaults to `true`.
  * `closeIcon?: string`The icon displayed in the close button. Defaults to `appConfig.ui.icons.close`.
  * `dismissible?: boolean`When `false`, the modal will not close when clicking outside or pressing escape. Defaults to `true`.
  * `class?: any`
  * `ui?: { overlay?: ClassNameValue; content?: ClassNameValue; header?: ClassNameValue; wrapper?: ClassNameValue; body?: ClassNameValue; footer?: ClassNameValue; title?: ClassNameValue; description?: ClassNameValue; close?: ClassNameValue; }`
  * `open?: boolean`The controlled open state of the dialog. Can be binded as `v-model:open`.
  * `defaultOpen?: boolean`The open state of the dialog when it is initially rendered. Use when you do not need to control its open state.
  * `modal?: boolean`The modality of the dialog When set to `true`,   
interaction with outside elements will be disabled and only dialog content
will be visible to screen readers.

  * `title?: string`
  * `description?: string`
  * `content?: (DialogContentProps & Partial<EmitsToProps<DialogContentImplEmits>>)`The content of the modal.
  * `overlay?: boolean`Render an overlay behind the modal. Defaults to `true`.
  * `transition?: boolean`Animate the modal when opening or closing. Defaults to `true`.
  * `side?: "top" | "bottom" | "right" | "left"`The side of the slideover. Defaults to `'right'`.
  * `portal?: string | boolean | HTMLElement`Render the modal in a portal. Defaults to `true`.
  * `close?: boolean | Partial<ButtonProps>`Display a close button to dismiss the modal. `{ size: 'md', color: 'neutral', variant: 'ghost' }` Defaults to `true`.
  * `closeIcon?: string`The icon displayed in the close button. Defaults to `appConfig.ui.icons.close`.
  * `dismissible?: boolean`When `false`, the modal will not close when clicking outside or pressing escape. Defaults to `true`.
  * `class?: any`
  * `ui?: { overlay?: ClassNameValue; content?: ClassNameValue; header?: ClassNameValue; wrapper?: ClassNameValue; body?: ClassNameValue; footer?: ClassNameValue; title?: ClassNameValue; description?: ClassNameValue; close?: ClassNameValue; }`
  * `open?: boolean`The controlled open state of the dialog. Can be binded as `v-model:open`.
  * `defaultOpen?: boolean`The open state of the dialog when it is initially rendered. Use when you do not need to control its open state.
  * `modal?: boolean`The modality of the dialog When set to `true`,   
interaction with outside elements will be disabled and only dialog content
will be visible to screen readers.

  * `as?: any`The element or component this component should render as. Defaults to `'div'`.
  * `title?: string`
  * `description?: string`
  * `inset?: boolean`Whether to inset the drawer from the edges. Defaults to `false`.
  * `content?: (DialogContentProps & Partial<EmitsToProps<DialogContentImplEmits>>)`The content of the modal.
  * `overlay?: boolean`Render an overlay behind the modal. Defaults to `true`.
  * `handle?: boolean`Render a handle on the drawer. Defaults to `true`.
  * `portal?: string | boolean | HTMLElement`Render the modal in a portal. Defaults to `true`.
  * `class?: any`
  * `ui?: { overlay?: ClassNameValue; content?: ClassNameValue; handle?: ClassNameValue; container?: ClassNameValue; header?: ClassNameValue; title?: ClassNameValue; description?: ClassNameValue; body?: ClassNameValue; footer?: ClassNameValue; }`
  * `fixed?: boolean`When `true`, don't move the drawer upwards if there's space, but rather only change it's height so it's fully scrollable when the keyboard is open
  * `open?: boolean`
  * `defaultOpen?: boolean`The open state of the dialog when it is initially rendered. Use when you do not need to control its open state.
  * `modal?: boolean`The modality of the dialog When set to `true`,   
interaction with outside elements will be disabled and only dialog content
will be visible to screen readers.

  * `activeSnapPoint?: string | number | null`
  * `closeThreshold?: number`Number between 0 and 1 that determines when the drawer should be closed. Example: threshold of 0.5 would close the drawer if the user swiped for 50% of the height of the drawer or more.
  * `shouldScaleBackground?: boolean`
  * `setBackgroundColorOnScale?: boolean`When `false` we don't change body's background color when the drawer is open.
  * `scrollLockTimeout?: number`Duration for which the drawer is not draggable after scrolling content inside of the drawer.
  * `dismissible?: boolean`When `false`, the modal will not close when clicking outside or pressing escape. Defaults to `true`.
  * `nested?: boolean`
  * `direction?: DrawerDirection`Direction of the drawer. Can be `top` or `bottom`, `left`, `right`.
  * `noBodyStyles?: boolean`When `true` the `body` doesn't get any styles assigned from Vaul
  * `handleOnly?: boolean`When `true` only allows the drawer to be dragged by the `<Drawer.Handle />` component.
  * `preventScrollRestoration?: boolean`
  * `snapPoints?: (string | number)[]`Array of numbers from 0 to 100 that corresponds to % of the screen a given snap point should take up. Should go from least visible. Example `[0.2, 0.5, 0.8]`. You can also use px values, which doesn't take screen height into account.

  
`toggle`| `true`| `boolean | Partial<ButtonProps>`Customize the toggle button to open the sidebar. `{ color: 'neutral', variant: 'ghost' }`  
`toggleSide`| `'left'`| ` "right" | "left"`The side to render the toggle button on.  
`collapsible`| `false`| `boolean`Whether to allow the user to collapse the
panel.  
`id`| `useId()`| ` string`The id of the panel.  
`side`| `'left'`| ` "right" | "left"`The side to render the panel on.  
`minSize`| `10`| ` number`The minimum size of the panel.  
`maxSize`| `20`| ` number`The maximum size of the panel.  
`defaultSize`| `15`| ` number`The default size of the panel.  
`resizable`| `false`| `boolean`Whether to allow the user to resize the panel.  
`collapsedSize`| `0`| ` number`The size of the panel when collapsed.  
`ui`| | ` { root?: ClassNameValue; header?: ClassNameValue; body?: ClassNameValue; footer?: ClassNameValue; toggle?: ClassNameValue; handle?: ClassNameValue; content?: ClassNameValue; overlay?: ClassNameValue; }`  
  
### Slots

Slot |  Type   
---|---  
`header`| `{ collapsed?: boolean | undefined; collapse?: ((value: boolean) => void) | undefined; }`  
`default`| `{ collapsed?: boolean | undefined; collapse?: ((value: boolean) => void) | undefined; }`  
`footer`| `{ collapsed?: boolean | undefined; collapse?: ((value: boolean) => void) | undefined; }`  
`toggle`| `{ open: boolean; toggle: () => void; }`  
`content`| `{}`  
`resize-handle`| `{ onMouseDown: (e: MouseEvent) => void; onTouchStart: (e:
TouchEvent) => void; }`  
  
## Theme

app.config.ts

    
    
    export default defineAppConfig({
      uiPro: {
        dashboardSidebar: {
          slots: {
            root: 'relative hidden lg:flex flex-col min-h-svh min-w-16 w-(--width) shrink-0',
            header: 'h-(--ui-header-height) shrink-0 flex items-center gap-1.5 px-4',
            body: 'flex flex-col gap-4 flex-1 overflow-y-auto px-4 py-2',
            footer: 'shrink-0 flex items-center gap-1.5 px-4 py-2',
            toggle: '',
            handle: '',
            content: 'lg:hidden',
            overlay: 'lg:hidden'
          },
          variants: {
            menu: {
              true: {
                header: 'sm:px-6',
                body: 'sm:px-6',
                footer: 'sm:px-6'
              }
            },
            side: {
              left: {
                root: 'border-r border-default'
              },
              right: {
                root: ''
              }
            },
            toggleSide: {
              left: {
                toggle: ''
              },
              right: {
                toggle: 'ms-auto'
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
            dashboardSidebar: {
              slots: {
                root: 'relative hidden lg:flex flex-col min-h-svh min-w-16 w-(--width) shrink-0',
                header: 'h-(--ui-header-height) shrink-0 flex items-center gap-1.5 px-4',
                body: 'flex flex-col gap-4 flex-1 overflow-y-auto px-4 py-2',
                footer: 'shrink-0 flex items-center gap-1.5 px-4 py-2',
                toggle: '',
                handle: '',
                content: 'lg:hidden',
                overlay: 'lg:hidden'
              },
              variants: {
                menu: {
                  true: {
                    header: 'sm:px-6',
                    body: 'sm:px-6',
                    footer: 'sm:px-6'
                  }
                },
                side: {
                  left: {
                    root: 'border-r border-default'
                  },
                  right: {
                    root: ''
                  }
                },
                toggleSide: {
                  left: {
                    toggle: ''
                  },
                  right: {
                    toggle: 'ms-auto'
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
            dashboardSidebar: {
              slots: {
                root: 'relative hidden lg:flex flex-col min-h-svh min-w-16 w-(--width) shrink-0',
                header: 'h-(--ui-header-height) shrink-0 flex items-center gap-1.5 px-4',
                body: 'flex flex-col gap-4 flex-1 overflow-y-auto px-4 py-2',
                footer: 'shrink-0 flex items-center gap-1.5 px-4 py-2',
                toggle: '',
                handle: '',
                content: 'lg:hidden',
                overlay: 'lg:hidden'
              },
              variants: {
                menu: {
                  true: {
                    header: 'sm:px-6',
                    body: 'sm:px-6',
                    footer: 'sm:px-6'
                  }
                },
                side: {
                  left: {
                    root: 'border-r border-default'
                  },
                  right: {
                    root: ''
                  }
                },
                toggleSide: {
                  left: {
                    toggle: ''
                  },
                  right: {
                    toggle: 'ms-auto'
                  }
                }
              }
            }
          }
        })
      ]
    })
    

Expand code

[DashboardSearchButtonA pre-styled Button to open the DashboardSearch
modal.](/components/dashboard-search-button)[DashboardSidebarCollapseA Button
to collapse the sidebar on desktop.](/components/dashboard-sidebar-collapse)


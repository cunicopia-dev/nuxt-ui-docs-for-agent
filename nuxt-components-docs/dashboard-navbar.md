<!-- source: https://ui.nuxt.com/components/dashboard-navbar --> # DashboardNavbarPRO

[GitHub](https://github.com/nuxt/ui-
pro/tree/v3/src/runtime/components/DashboardNavbar.vue)

A responsive navbar to display in a dashboard.

## Usage

The DashboardNavbar component is a responsive navigation bar that integrates
with the [DashboardSidebar](/components/dashboard-sidebar) component. It
includes a mobile toggle button to enable responsive navigation in dashboard
layouts.

Use it inside the `header` slot of the [DashboardPanel](/components/dashboard-
panel) component:

pages/index.vue

    
    
    <script setup lang="ts">
    definePageMeta({
      layout: 'dashboard'
    })
    </script>
    
    <template>
      <UDashboardPanel>
        <template #header>
          <UDashboardNavbar />
        </template>
      </UDashboardPanel>
    </template>
    

Use the `left`, `default` and `right` slots to customize the navbar.

# Inbox

4

AllUnread

    
    
    <script setup lang="ts">
    import type { TabsItem } from '@nuxt/ui'
    
    const items: TabsItem[] = [
      {
        label: 'All',
        value: 'all'
      },
      {
        label: 'Unread',
        value: 'unread'
      }
    ]
    </script>
    
    <template>
      <UDashboardNavbar title="Inbox">
        <template #leading>
          <UDashboardSidebarCollapse />
        </template>
    
        <template #trailing>
          <UBadge label="4" variant="subtle" />
        </template>
    
        <template #right>
          <UTabs :items="items" default-value="all" size="sm" class="w-40" :content="false" />
        </template>
      </UDashboardNavbar>
    </template>
    

In this example, we use the [Tabs](/components/tabs) component in the right
slot to display some tabs.

### Title

Use the `title` prop to set the title of the navbar.

title

# Dashboard

    
    
    <template>
      <UDashboardNavbar title="Dashboard" />
    </template>
    

### Icon

Use the `icon` prop to set the icon of the navbar.

icon

# Dashboard

    
    
    <template>
      <UDashboardNavbar title="Dashboard" icon="i-lucide-house" />
    </template>
    

### Toggle

Use the `toggle` prop to customize the toggle button displayed on mobile that
opens the [DashboardSidebar](/components/dashboard-sidebar) component.

You can pass any property from the [Button](/components/button) component to
customize it.

    
    
    <template>
      <UDashboardNavbar
        title="Dashboard"
        :toggle="{
          color: 'primary',
          variant: 'subtle',
          class: 'rounded-full'
        }"
      />
    </template>
    

### Toggle Side

Use the `toggle-side` prop to change the side of the toggle button. Defaults
to `right`.

    
    
    <template>
      <UDashboardNavbar
        title="Dashboard"
        toggle-side="right"
      />
    </template>
    

## API

### Props

Prop |  Default |  Type   
---|---|---  
`as`| `'div'`| `any`The element or component this component should render as.  
`toggle`| `true`| `boolean | Partial<ButtonProps>`  
`toggleSide`| `'left'`| ` "right" | "left"`  
`icon`| | ` string`The icon displayed next to the title.  
`title`| | ` string`  
`ui`| | ` { root?: ClassNameValue; left?: ClassNameValue; icon?: ClassNameValue; title?: ClassNameValue; center?: ClassNameValue; right?: ClassNameValue; toggle?: ClassNameValue; }`  
  
### Slots

Slot |  Type   
---|---  
`title`| `{}`  
`leading`| `DashboardNavbarSlotsProps`  
`trailing`| `DashboardNavbarSlotsProps`  
`left`| `DashboardNavbarSlotsProps`  
`default`| `DashboardNavbarSlotsProps`  
`right`| `DashboardNavbarSlotsProps`  
`toggle`| `DashboardNavbarSlotsProps`  
  
## Theme

app.config.ts

    
    
    export default defineAppConfig({
      uiPro: {
        dashboardNavbar: {
          slots: {
            root: 'h-(--ui-header-height) shrink-0 flex items-center justify-between border-b border-default px-4 sm:px-6 gap-1.5',
            left: 'flex items-center gap-1.5 min-w-0',
            icon: 'shrink-0 size-5 self-center me-1.5',
            title: 'flex items-center gap-1.5 font-semibold text-highlighted truncate',
            center: 'hidden lg:flex',
            right: 'flex items-center shrink-0 gap-1.5',
            toggle: ''
          },
          variants: {
            toggleSide: {
              left: {
                toggle: ''
              },
              right: {
                toggle: ''
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
            dashboardNavbar: {
              slots: {
                root: 'h-(--ui-header-height) shrink-0 flex items-center justify-between border-b border-default px-4 sm:px-6 gap-1.5',
                left: 'flex items-center gap-1.5 min-w-0',
                icon: 'shrink-0 size-5 self-center me-1.5',
                title: 'flex items-center gap-1.5 font-semibold text-highlighted truncate',
                center: 'hidden lg:flex',
                right: 'flex items-center shrink-0 gap-1.5',
                toggle: ''
              },
              variants: {
                toggleSide: {
                  left: {
                    toggle: ''
                  },
                  right: {
                    toggle: ''
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
            dashboardNavbar: {
              slots: {
                root: 'h-(--ui-header-height) shrink-0 flex items-center justify-between border-b border-default px-4 sm:px-6 gap-1.5',
                left: 'flex items-center gap-1.5 min-w-0',
                icon: 'shrink-0 size-5 self-center me-1.5',
                title: 'flex items-center gap-1.5 font-semibold text-highlighted truncate',
                center: 'hidden lg:flex',
                right: 'flex items-center shrink-0 gap-1.5',
                toggle: ''
              },
              variants: {
                toggleSide: {
                  left: {
                    toggle: ''
                  },
                  right: {
                    toggle: ''
                  }
                }
              }
            }
          }
        })
      ]
    })
    

Expand code

[DashboardGroupA fixed layout component that provides context for dashboard
components with sidebar state management and
persistence.](/components/dashboard-group)[DashboardPanelA resizable panel to
display in a dashboard.](/components/dashboard-panel)


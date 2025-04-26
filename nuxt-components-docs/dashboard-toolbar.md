<!-- source: https://ui.nuxt.com/components/dashboard-toolbar --> # DashboardToolbarPRO

[GitHub](https://github.com/nuxt/ui-
pro/tree/v3/src/runtime/components/DashboardToolbar.vue)

A toolbar to display under the navbar in a dashboard.

## Usage

The DashboardToolbar component is used to display a toolbar under the
[DashboardNavbar](/components/dashboard-navbar) component.

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
    
          <UDashboardToolbar />
        </template>
      </UDashboardPanel>
    </template>
    

Use the `left`, `default` and `right` slots to customize the toolbar.

    
    
    <script setup lang="ts">
    import type { NavigationMenuItem } from '@nuxt/ui'
    
    const items: NavigationMenuItem[][] = [
      [
        {
          label: 'General',
          icon: 'i-lucide-user',
          active: true
        },
        {
          label: 'Members',
          icon: 'i-lucide-users'
        },
        {
          label: 'Notifications',
          icon: 'i-lucide-bell'
        }
      ],
      [
        {
          label: 'Documentation',
          icon: 'i-lucide-book-open',
          to: 'https://ui.nuxt.com/getting-started/installation/pro/nuxt',
          target: '_blank'
        },
        {
          label: 'Buy now',
          icon: 'i-lucide-shopping-cart',
          to: 'https://ui.nuxt.com/pro/purchase',
          target: '_blank'
        }
      ]
    ]
    </script>
    
    <template>
      <UDashboardToolbar>
        <UNavigationMenu :items="items" highlight class="flex-1" />
      </UDashboardToolbar>
    </template>
    

In this example, we use the [NavigationMenu](/components/navigation-menu)
component to render some links.

## API

### Props

Prop |  Default |  Type   
---|---|---  
`as`| `'div'`| `any`The element or component this component should render as.  
`ui`| | ` { root?: ClassNameValue; left?: ClassNameValue; right?: ClassNameValue; }`  
  
### Slots

Slot |  Type   
---|---  
`default`| `{}`  
`left`| `{}`  
`right`| `{}`  
  
## Theme

app.config.ts

    
    
    export default defineAppConfig({
      uiPro: {
        dashboardToolbar: {
          slots: {
            root: 'shrink-0 flex items-center justify-between border-b border-default px-4 sm:px-6 gap-1.5 overflow-x-auto min-h-[49px]',
            left: 'flex items-center gap-1.5',
            right: 'flex items-center gap-1.5'
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
            dashboardToolbar: {
              slots: {
                root: 'shrink-0 flex items-center justify-between border-b border-default px-4 sm:px-6 gap-1.5 overflow-x-auto min-h-[49px]',
                left: 'flex items-center gap-1.5',
                right: 'flex items-center gap-1.5'
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
            dashboardToolbar: {
              slots: {
                root: 'shrink-0 flex items-center justify-between border-b border-default px-4 sm:px-6 gap-1.5 overflow-x-auto min-h-[49px]',
                left: 'flex items-center gap-1.5',
                right: 'flex items-center gap-1.5'
              }
            }
          }
        })
      ]
    })
    

Expand code

[DashboardSidebarToggleA Button to toggle the sidebar on
mobile.](/components/dashboard-sidebar-toggle)[DrawerA drawer that smoothly
slides in & out of the screen.](/components/drawer)


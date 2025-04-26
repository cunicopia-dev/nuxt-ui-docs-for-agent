<!-- source: https://ui.nuxt.com/components/dashboard-group --> # DashboardGroupPRO

[GitHub](https://github.com/nuxt/ui-
pro/tree/v3/src/runtime/components/DashboardGroup.vue)

A fixed layout component that provides context for dashboard components with
sidebar state management and persistence.

## Usage

The DashboardGroup component is the main layout that wraps the
[DashboardSidebar](/components/dashboard-sidebar) and
[DashboardPanel](/components/dashboard-panel) components to create a
responsive dashboard interface.

Use it in a layout or in your `app.vue`:

layouts/dashboard.vue

    
    
    <template>
      <UDashboardGroup>
        <UDashboardSidebar />
    
        <slot />
      </UDashboardGroup>
    </template>
    

## API

### Props

Prop |  Default |  Type   
---|---|---  
`as`| `'div'`| `any`The element or component this component should render as.  
`storage`| `'cookie'`| ` "cookie" | "local"`  
`storageKey`| `'dashboard'`| ` string`  
`persistent`| `true`| `boolean`  
`unit`| `'%'`| ` "%" | "rem" | "px"`  
  
### Slots

Slot |  Type   
---|---  
`default`| `{}`  
  
## Theme

app.config.ts

    
    
    export default defineAppConfig({
      uiPro: {
        dashboardGroup: {
          base: 'fixed inset-0 flex overflow-hidden'
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
            dashboardGroup: {
              base: 'fixed inset-0 flex overflow-hidden'
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
            dashboardGroup: {
              base: 'fixed inset-0 flex overflow-hidden'
            }
          }
        })
      ]
    })
    

Expand code

[ContextMenuA menu to display actions when right-clicking on an
element.](/components/context-menu)[DashboardNavbarA responsive navbar to
display in a dashboard.](/components/dashboard-navbar)


<!-- source: https://ui.nuxt.com/components/dashboard-sidebar-collapse --> # DashboardSidebarCollapsePRO

[Button](/components/button)[GitHub](https://github.com/nuxt/ui-
pro/tree/v3/src/runtime/components/DashboardSidebarCollapse.vue)

A Button to collapse the sidebar on desktop.

## Usage

The DashboardSidebarCollapse component is used to collapse/expand the
[DashboardSidebar](/components/dashboard-sidebar) component **when
its`collapsible` prop is set**.

    
    
    <template>
      <UDashboardSidebarCollapse />
    </template>
    

It extends the [Button](/components/button) component, so you can pass any
property such as `color`, `variant`, `size`, etc.

    
    
    <template>
      <UDashboardSidebarCollapse variant="subtle" />
    </template>
    

The button defaults to `color="neutral"` and `variant="ghost"`.

## Examples

### Within `header` slot

You can put this component in the `header` slot of the
[DashboardSidebar](/components/dashboard-sidebar) component and use the
`collapsed` prop to hide the left part of the header for example:

layouts/dashboard.vue

    
    
    <template>
      <UDashboardGroup>
        <UDashboardSidebar collapsible>
          <template #header="{ collapsed }">
            <Logo v-if="!collapsed" />
    
            <UDashboardSidebarCollapse variant="subtle" />
          </template>
        </UDashboardSidebar>
    
        <slot />
      </UDashboardGroup>
    </template>
    

### Within `leading` slot

You can put this component in the `leading` slot of the
[DashboardNavbar](/components/dashboard-navbar) component to display it before
the title for example:

pages/index.vue

    
    
    <script setup lang="ts">
    definePageMeta({
      layout: 'dashboard'
    })
    </script>
    
    <template>
      <UDashboardPanel>
        <template #header>
          <UDashboardNavbar title="Home">
            <template #leading>
              <UDashboardSidebarCollapse variant="subtle" />
            </template>
          </UDashboardNavbar>
        </template>
      </UDashboardPanel>
    </template>
    

## API

### Props

Prop |  Default |  Type   
---|---|---  
`as`| `'button'`| `any`The element or component this component should render
as when not a link.  
`color`| `'neutral'`| ` "error" | "primary" | "secondary" | "success" | "info" | "warning" | "neutral"`  
`variant`| `'ghost'`| ` "link" | "solid" | "outline" | "soft" | "subtle" | "ghost"`  
`side`| `'left'`| ` "right" | "left"`  
`disabled`| | `boolean`  
`size`| `'md'`| ` "md" | "xs" | "sm" | "lg" | "xl"`  
`ui`| | ` { base?: ClassNameValue; label?: ClassNameValue; leadingIcon?: ClassNameValue; leadingAvatar?: ClassNameValue; leadingAvatarSize?: ClassNameValue; trailingIcon?: ClassNameValue; }`  
  
## Theme

app.config.ts

    
    
    export default defineAppConfig({
      uiPro: {
        dashboardSidebarCollapse: {
          base: 'hidden lg:flex',
          variants: {
            side: {
              left: '',
              right: ''
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
            dashboardSidebarCollapse: {
              base: 'hidden lg:flex',
              variants: {
                side: {
                  left: '',
                  right: ''
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
            dashboardSidebarCollapse: {
              base: 'hidden lg:flex',
              variants: {
                side: {
                  left: '',
                  right: ''
                }
              }
            }
          }
        })
      ]
    })
    

Expand code

[DashboardSidebarA resizable and collapsible sidebar to display in a
dashboard.](/components/dashboard-sidebar)[DashboardSidebarToggleA Button to
toggle the sidebar on mobile.](/components/dashboard-sidebar-toggle)


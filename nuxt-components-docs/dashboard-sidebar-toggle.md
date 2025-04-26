<!-- source: https://ui.nuxt.com/components/dashboard-sidebar-toggle --> # DashboardSidebarTogglePRO

[Button](/components/button)[GitHub](https://github.com/nuxt/ui-
pro/tree/v3/src/runtime/components/DashboardSidebarToggle.vue)

Customize the toggle button to open the sidebar. `{ color: 'neutral', variant:
'ghost' }`

## Usage

The DashboardSidebarToggle component is used by the
[DashboardNavbar](/components/dashboard-navbar) and
[DashboardSidebar](/components/dashboard-sidebar) components.

It is automatically displayed on mobile to toggle the sidebar, **you don't
have to add it manually**.

    
    
    <template>
      <UDashboardSidebarToggle />
    </template>
    

It extends the [Button](/components/button) component, so you can pass any
property such as `color`, `variant`, `size`, etc.

    
    
    <template>
      <UDashboardSidebarToggle variant="subtle" />
    </template>
    

The button defaults to `color="neutral"` and `variant="ghost"`.

## Examples

### Within `toggle` slot

Even though this component is automatically displayed on mobile, you can use
the `toggle` slot of the [DashboardNavbar](/components/dashboard-navbar) and
[DashboardSidebar](/components/dashboard-sidebar) components to customize the
button.

layouts/dashboard.vuepages/index.vue

    
    
    <template>
      <UDashboardGroup>
        <UDashboardSidebar>
          <template #toggle>
            <UDashboardSidebarToggle variant="subtle" />
          </template>
        </UDashboardSidebar>
    
        <slot />
      </UDashboardGroup>
    </template>
    
    
    
    <script setup lang="ts">
    definePageMeta({
      layout: 'dashboard'
    })
    </script>
    
    <template>
      <UDashboardPanel>
        <template #header>
          <UDashboardNavbar title="Home">
            <template #toggle>
              <UDashboardSidebarToggle variant="subtle" />
            </template>
          </UDashboardNavbar>
        </template>
      </UDashboardPanel>
    </template>
    

When using the `toggle-side` prop of the `DashboardSidebar` and
`DashboardNavbar` components, the button will be displayed on the specified
side.

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
        dashboardSidebarToggle: {
          base: 'lg:hidden',
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
            dashboardSidebarToggle: {
              base: 'lg:hidden',
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
            dashboardSidebarToggle: {
              base: 'lg:hidden',
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

[DashboardSidebarCollapseA Button to collapse the sidebar on
desktop.](/components/dashboard-sidebar-collapse)[DashboardToolbarA toolbar to
display under the navbar in a dashboard.](/components/dashboard-toolbar)


<!-- source: https://ui.nuxt.com/components/dashboard-resize-handle --> # DashboardResizeHandlePRO

[GitHub](https://github.com/nuxt/ui-
pro/tree/v3/src/runtime/components/DashboardResizeHandle.vue)

A handle to resize a sidebar or panel.

## Usage

The DashboardResizeHandle component is used by the
[DashboardSidebar](/components/dashboard-sidebar) and
[DashboardPanel](/components/dashboard-panel) components.

It is automatically displayed when the `resizable` prop is set, **you don't
have to add it manually**.

## Examples

### Within `resize-handle` slot

Even though this component is automatically displayed when the `resizable`
prop is set, you can use the `resize-handle` slot of the
[DashboardSidebar](/components/dashboard-sidebar) and
[DashboardPanel](/components/dashboard-panel) components to customize the
handle.

layouts/dashboard.vuepages/index.vue

    
    
    <template>
      <UDashboardGroup>
        <UDashboardSidebar resizable>
          <template #resize-handle="{ onMouseDown, onTouchStart }">
            <UDashboardResizeHandle
              class="after:absolute after:inset-y-0 after:right-0 after:w-px hover:after:bg-(--ui-border-accented) after:transition"
              @mousedown="onMouseDown"
              @touchstart="onTouchStart"
            />
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
      <UDashboardPanel resizable>
        <template #resize-handle="{ onMouseDown, onTouchStart }">
          <UDashboardResizeHandle
            class="after:absolute after:inset-y-0 after:right-0 after:w-px hover:after:bg-(--ui-border-accented) after:transition"
            @mousedown="onMouseDown"
            @touchstart="onTouchStart"
          />
        </template>
      </UDashboardPanel>
    </template>
    

In this example, we add an `after` pseudo-element to display a vertical line
on hover.

## API

### Props

Prop |  Default |  Type   
---|---|---  
`as`| `'div'`| `any`The element or component this component should render as.  
  
### Slots

Slot |  Type   
---|---  
`default`| `{}`  
  
## Theme

app.config.ts

    
    
    export default defineAppConfig({
      uiPro: {
        dashboardResizeHandle: {
          base: 'hidden lg:block touch-none select-none cursor-ew-resize relative before:absolute before:inset-y-0 before:-left-1.5 before:-right-1.5'
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
            dashboardResizeHandle: {
              base: 'hidden lg:block touch-none select-none cursor-ew-resize relative before:absolute before:inset-y-0 before:-left-1.5 before:-right-1.5'
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
            dashboardResizeHandle: {
              base: 'hidden lg:block touch-none select-none cursor-ew-resize relative before:absolute before:inset-y-0 before:-left-1.5 before:-right-1.5'
            }
          }
        })
      ]
    })
    

Expand code

[DashboardPanelA resizable panel to display in a
dashboard.](/components/dashboard-panel)[DashboardSearchA ready to use
CommandPalette to add to your dashboard.](/components/dashboard-search)


<!-- source: https://ui.nuxt.com/components/dashboard-panel --> # DashboardPanelPRO

[GitHub](https://github.com/nuxt/ui-
pro/tree/v3/src/runtime/components/DashboardPanel.vue)

A resizable panel to display in a dashboard.

## Usage

The DashboardPanel component is used to display a panel. Its state (size,
collapsed, etc.) will be saved based on the `storage` and `storage-key` props
you provide to the [DashboardGroup](/components/dashboard-group#props)
component.

Use it inside the default slot of the [DashboardGroup](/components/dashboard-
group) component, you can put multiple panels next to each other:

pages/index.vue

    
    
    <script setup lang="ts">
    definePageMeta({
      layout: 'dashboard'
    })
    </script>
    
    <template>
      <UDashboardPanel id="inbox-1" resizable />
    
      <UDashboardPanel id="inbox-2" class="hidden lg:flex" />
    </template>
    

It is recommended to set an `id` when using multiple panels in different pages
to avoid conflicts.

Use the `header`, `body` and `footer` slots to customize the panel or the
default slot if you don't want a scrollable body with padding.

# Inbox

    
    
    <template>
      <UDashboardPanel resizable>
        <template #header>
          <UDashboardNavbar title="Inbox">
            <template #leading>
              <UDashboardSidebarCollapse />
            </template>
          </UDashboardNavbar>
        </template>
    
        <template #body>
          <Placeholder class="h-full" />
        </template>
      </UDashboardPanel>
    </template>
    

Expand code

Most of the time, you will use the [`DashboardNavbar`](/components/dashboard-
navbar) component in the `header` slot.

### Resizable

Use the `resizable` prop to make the panel resizable.

resizable

true

    
    
    <template>
      <UDashboardPanel resizable>
        <template #body>
          <Placeholder class="h-96" />
        </template>
      </UDashboardPanel>
    </template>
    

### Size

Use the `min-size`, `max-size` and `default-size` props to customize the size
of the panel.

minSize

defaultSize

maxSize

    
    
    <template>
      <UDashboardPanel resizable>
        <template #body>
          <Placeholder class="h-96" />
        </template>
      </UDashboardPanel>
    </template>
    

## API

### Props

Prop |  Default |  Type   
---|---|---  
`minSize`| `15`| ` number`  
`resizable`| `false`| `boolean`  
`id`| `useId()`| ` string`The id of the panel.  
`maxSize`| `100`| ` number`The maximum size of the panel.  
`defaultSize`| `0`| ` number`The default size of the panel.  
`ui`| | ` { root?: ClassNameValue; body?: ClassNameValue; handle?: ClassNameValue; }`  
  
### Slots

Slot |  Type   
---|---  
`default`| `{}`  
`header`| `{}`  
`body`| `{}`  
`footer`| `{}`  
`resize-handle`| `{ onMouseDown: (e: MouseEvent) => void; onTouchStart: (e:
TouchEvent) => void; }`  
  
## Theme

app.config.ts

    
    
    export default defineAppConfig({
      uiPro: {
        dashboardPanel: {
          slots: {
            root: 'relative flex flex-col min-w-0 min-h-svh lg:not-last:border-r lg:not-last:border-default shrink-0',
            body: 'flex flex-col gap-4 sm:gap-6 flex-1 overflow-y-auto p-4 sm:p-6',
            handle: ''
          },
          variants: {
            size: {
              true: {
                root: 'w-full lg:w-(--width)'
              },
              false: {
                root: 'flex-1'
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
            dashboardPanel: {
              slots: {
                root: 'relative flex flex-col min-w-0 min-h-svh lg:not-last:border-r lg:not-last:border-default shrink-0',
                body: 'flex flex-col gap-4 sm:gap-6 flex-1 overflow-y-auto p-4 sm:p-6',
                handle: ''
              },
              variants: {
                size: {
                  true: {
                    root: 'w-full lg:w-(--width)'
                  },
                  false: {
                    root: 'flex-1'
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
            dashboardPanel: {
              slots: {
                root: 'relative flex flex-col min-w-0 min-h-svh lg:not-last:border-r lg:not-last:border-default shrink-0',
                body: 'flex flex-col gap-4 sm:gap-6 flex-1 overflow-y-auto p-4 sm:p-6',
                handle: ''
              },
              variants: {
                size: {
                  true: {
                    root: 'w-full lg:w-(--width)'
                  },
                  false: {
                    root: 'flex-1'
                  }
                }
              }
            }
          }
        })
      ]
    })
    

Expand code

[DashboardNavbarA responsive navbar to display in a
dashboard.](/components/dashboard-navbar)[DashboardResizeHandleA handle to
resize a sidebar or panel.](/components/dashboard-resize-handle)


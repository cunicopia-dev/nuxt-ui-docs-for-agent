<!-- source: https://ui.nuxt.com/components/dashboard-search-button --> # DashboardSearchButtonPRO

[Button](/components/button)[GitHub](https://github.com/nuxt/ui-
pro/tree/v3/src/runtime/components/DashboardSearchButton.vue)

A pre-styled Button to open the DashboardSearch modal.

## Usage

The DashboardSearchButton component is used to open the
[DashboardSearch](/components/dashboard-search) modal.

Search...

` ``K`

    
    
    <template>
      <UDashboardSearchButton />
    </template>
    

It extends the [Button](/components/button) component, so you can pass any
property such as `color`, `variant`, `size`, etc.

Search...

` ``K`

    
    
    <template>
      <UDashboardSearchButton variant="subtle" />
    </template>
    

The button defaults to `color="neutral"` and `variant="outline"` when not
collapsed, `variant="ghost"` when collapsed.

### Collapsed

Use the `collapsed` prop to hide the button's label and kbds. Defaults to
`false`.

collapsed

true

    
    
    <template>
      <UDashboardSearchButton collapsed />
    </template>
    

[](/components/dashboard-sidebar#slots)When using the button in the
**DashboardSidebar** component, use the `collapsed` slot prop directly.

### Kbds

Use the `kbds` prop to display keyboard keys in the button. Defaults to
`['meta', 'K']` to match the default shortcut of the
[DashboardSearch](/components/dashboard-search#shortcut) component.

collapsed

false

Search...

` ``O`

    
    
    <template>
      <UDashboardSearchButton :kbds="['alt', 'O']" />
    </template>
    

## API

### Props

Prop |  Default |  Type   
---|---|---  
`color`| `'neutral'`| ` "error" | "primary" | "secondary" | "success" | "info" | "warning" | "neutral"`  
`collapsed`| `false`| `boolean`  
`kbds`| `["meta", "k"]`| ` (string | undefined)[] | KbdProps[]`Show properties

  * `as?: any`The element or component this component should render as. Defaults to `'kbd'`.
  * `value?: string`
  * `variant?: "solid" | "outline" | "subtle"`Defaults to `'outline'`.
  * `size?: "md" | "sm" | "lg"`Defaults to `'md'`.
  * `class?: any`

  
`icon`| `appConfig.ui.icons.search`| ` string`The icon displayed in the
button.  
`label`| `t('dashboardSearchButton.label')`| ` string`The label displayed in
the button.  
`size`| | ` "md" | "xs" | "sm" | "lg" | "xl"`  
`variant`| | ` "link" | "solid" | "outline" | "soft" | "subtle" | "ghost"`The variant of the button. Defaults to 'outline' when not collapsed, 'ghost' when collapsed.  
`ui`| | ` { base?: ClassNameValue; trailing?: ClassNameValue; } & { base?: ClassNameValue; label?: ClassNameValue; leadingIcon?: ClassNameValue; leadingAvatar?: ClassNameValue; leadingAvatarSize?: ClassNameValue; trailingIcon?: ClassNameValue; }`Show properties

  * `base?: ClassNameValue`
  * `trailing?: ClassNameValue`
  * `label?: ClassNameValue`
  * `leadingIcon?: ClassNameValue`
  * `leadingAvatar?: ClassNameValue`
  * `leadingAvatarSize?: ClassNameValue`
  * `trailingIcon?: ClassNameValue`

  
  
### Slots

Slot |  Type   
---|---  
`leading`| `{}`  
`default`| `{}`  
`trailing`| `{}`  
  
## Theme

app.config.ts

    
    
    export default defineAppConfig({
      uiPro: {
        dashboardSearchButton: {
          slots: {
            base: '',
            trailing: 'hidden lg:flex items-center gap-0.5 ms-auto'
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
            dashboardSearchButton: {
              slots: {
                base: '',
                trailing: 'hidden lg:flex items-center gap-0.5 ms-auto'
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
            dashboardSearchButton: {
              slots: {
                base: '',
                trailing: 'hidden lg:flex items-center gap-0.5 ms-auto'
              }
            }
          }
        })
      ]
    })
    

Expand code

[DashboardSearchA ready to use CommandPalette to add to your
dashboard.](/components/dashboard-search)[DashboardSidebarA resizable and
collapsible sidebar to display in a dashboard.](/components/dashboard-sidebar)


<!-- source: https://ui.nuxt.com/components/color-mode-switch --> # ColorModeSwitchPRO

[Switch](/components/switch)[GitHub](https://github.com/nuxt/ui-
pro/blob/v3/src/runtime/components/color-mode/ColorModeSwitch.vue)

A switch to toggle between light and dark mode.

## Usage

The ColorModeSwitch component extends the [Switch](/components/switch)
component, so you can pass any property such as `color`, `size`, etc.

    
    
    <template>
      <UColorModeSwitch />
    </template>
    

## Examples

### With custom icons

Use the `app.config.ts` to customize the icon with the `ui.icons` property:

app.config.ts

    
    
    export default defineAppConfig({
      ui: {
        icons: {
          light: 'i-ph-sun',
          dark: 'i-ph-moon'
        }
      }
    })
    

Use the `vite.config.ts` to customize the icon with the `ui.icons` property:

vite.config.ts

    
    
    import { defineConfig } from 'vite'
    import vue from '@vitejs/plugin-vue'
    import ui from '@nuxt/ui/vite'
    
    export default defineConfig({
      plugins: [
        vue(),
        ui({
          ui: {
            icons: {
              light: 'i-ph-sun',
              dark: 'i-ph-moon'
            }
          }
        })
      ]
    })
    

## API

### Props

Prop |  Default |  Type   
---|---|---  
`as`| `'div'`| `any`The element or component this component should render as.  
`disabled`| | `boolean`When `true`, prevents the user from interacting with the switch.  
`color`| `'primary'`| ` "error" | "primary" | "secondary" | "success" | "info" | "warning" | "neutral"`  
`size`| `'md'`| ` "md" | "xs" | "sm" | "lg" | "xl"`  
`ui`| | ` { root?: ClassNameValue; base?: ClassNameValue; container?: ClassNameValue; thumb?: ClassNameValue; icon?: ClassNameValue; wrapper?: ClassNameValue; label?: ClassNameValue; description?: ClassNameValue; }`  
  
[ColorModeSelectA Select to switch between system, dark & light
mode.](/components/color-mode-select)[ColorPickerA component to select a
color.](/components/color-picker)

